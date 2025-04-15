import os
import json
import zipfile
from flask import Flask, request, jsonify, render_template, send_file

app = Flask(__name__, template_folder="templates")

UPLOAD_DIR = "usl_web_uploads"
OUTPUT_DIR = "usl_outputs"
SYNTAX_FILE = "syntax_templates_fully_extended.json"
REFERENCE_FILE = "usl_symbol_reference_i18n_extended.json"
TRANSLATIONS_FILE = "translations_extended.json"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_syntax():
    with open(SYNTAX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def parse_usl_lines(lines, lang):
    matched, fallback = [], []
    for line in lines:
        line = line.strip()
        if line.startswith(f"Symbolic[{lang}]"):
            matched.append(line.split("]:", 1)[-1].strip())
        elif line.startswith("Symbolic:"):
            fallback.append(line.split(":", 1)[-1].strip())
    return matched if matched else fallback

def generate_safe(template, *values):
    try:
        needed = template.count("{}")
        return template.format(*([*values] * needed)[:needed])
    except:
        return "// Invalid template"

def transpile(lines, lang, syntax):
    struct = syntax.get(lang, {}).get("structure", {})
    comment = struct.get("comment", "# {}")
    exts = syntax.get(lang, {}).get("file_extensions", [])
    ext = exts[0] if exts else lang[:3]
    filename = f"{lang}.{ext}"
    output_path = os.path.join(OUTPUT_DIR, filename)
    parsed = parse_usl_lines(lines, lang)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(comment.format(f"This is {lang} syntax") + "\n")
        for symbolic in parsed:
            try:
                if "print(" in symbolic:
                    value = symbolic.split("print(", 1)[1].split(")", 1)[0]
                    f.write(generate_safe(struct.get("print", "{}"), value) + "\n")
                elif "let " in symbolic and "=" in symbolic:
                    assign = symbolic.split("let ", 1)[1]
                    left, right = assign.split("=", 1)
                    f.write(generate_safe(struct.get("assign", "{} = {}"), left.strip(), right.strip()) + "\n")
                elif symbolic.startswith("if "):
                    f.write(generate_safe(struct.get("if", "if {}:\n    {}"), symbolic[3:], "pass") + "\n")
                elif symbolic.startswith("function "):
                    head = symbolic.split("function", 1)[-1].strip()
                    if "(" in head:
                        name, args = head.split("(", 1)
                        f.write(generate_safe(struct.get("function", "def {}({}):\n    {}"), name.strip(), args.rstrip(")"), "pass") + "\n")
                    else:
                        f.write(comment.format("Invalid function format: " + symbolic) + "\n")
                elif symbolic.startswith("return "):
                    f.write(generate_safe(struct.get("return", "return {}"), symbolic[7:].strip()) + "\n")
                elif symbolic.startswith("comment "):
                    f.write(generate_safe(struct.get("comment", "# {}"), symbolic[8:].strip().strip('"')) + "\n")
                else:
                    f.write(comment.format("Unrecognized: " + symbolic) + "\n")
            except Exception as e:
                f.write(comment.format(f"Error: {e} in line: {symbolic}") + "\n")
    return filename

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/symbol_reference")
def symbol_reference():
    with open(REFERENCE_FILE, "r", encoding="utf-8") as f:
        return jsonify(json.load(f))

@app.route("/languages")
def get_languages():
    syntax = load_syntax()
    return jsonify(sorted(syntax.keys()))

@app.route("/process", methods=["POST"])
def process_file_or_form():
    syntax = load_syntax()
    results = {}
    uploaded_file = request.files.get("usl_file")
    input_text = request.form.get("usl_code", "")
    lines = uploaded_file.read().decode().splitlines() if uploaded_file else input_text.splitlines()
    languages = request.form.getlist("languages")

    for lang in languages:
        if lang == "usl":
            with open(os.path.join(OUTPUT_DIR, "usl_input_original.usl"), "w", encoding="utf-8") as f:
                f.writelines(line + "\n" for line in lines)
            results["usl"] = "\n".join(lines)
        else:
            filename = transpile(lines, lang, syntax)
            with open(os.path.join(OUTPUT_DIR, filename), "r", encoding="utf-8") as f:
                results[lang] = f.read()

    # Build ZIP of outputs
    zip_path = os.path.join(OUTPUT_DIR, "all_outputs.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for f in os.listdir(OUTPUT_DIR):
            if not f.endswith(".zip"):
                zipf.write(os.path.join(OUTPUT_DIR, f), arcname=f)

    return jsonify({ "success": True, "outputs": results })

@app.route("/download")
def download_all():
    zip_path = os.path.join(OUTPUT_DIR, "all_outputs.zip")
    if not os.path.exists(zip_path):
        return "No zip file found.", 404
    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
