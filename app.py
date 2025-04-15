
import os
import json
import zipfile
from flask import Flask, request, jsonify, render_template, send_file

app = Flask(__name__, template_folder="templates")
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
SYNTAX_FILE = "syntax_templates_fully_extended.json"
REFERENCE_FILE = "usl_symbol_reference_full_i18n.json"

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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/symbol_reference")
def symbol_reference():
    with open(REFERENCE_FILE, "r", encoding="utf-8") as f:
        return jsonify(json.load(f))

@app.route("/transpile", methods=["POST"])
def transpile():
    syntax = load_syntax()
    usl_input = request.json.get("uslInput", "")
    selected_langs = request.json.get("languages", [])
    outputs = {}

    lines = usl_input.splitlines()
    for lang in selected_langs:
        if lang not in syntax:
            outputs[lang] = "// Language not supported."
            continue

        struct = syntax[lang]["structure"]
        comment = struct.get("comment", "# {}")
        parsed = parse_usl_lines(lines, lang)
        result_lines = []

        for symbolic in parsed:
            try:
                if "print(" in symbolic:
                    val = symbolic.split("print(", 1)[1].split(")", 1)[0]
                    result_lines.append(generate_safe(struct.get("print", "{}"), val))
                elif "let " in symbolic:
                    assign = symbolic.split("let ", 1)[1]
                    left, right = assign.split("=")
                    result_lines.append(generate_safe(struct.get("assign", "{} = {}"), left.strip(), right.strip()))
                elif symbolic.startswith("if "):
                    cond = symbolic[3:]
                    result_lines.append(generate_safe(struct.get("if", "if {}:\n    {}"), cond.strip(), "pass"))
                elif symbolic.startswith("function "):
                    head = symbolic.split("function", 1)[-1].strip()
                    name, args = head.split("(", 1)
                    args = args.rstrip(")")
                    result_lines.append(generate_safe(struct.get("function", "def {}({}):\n    {}"), name.strip(), args.strip(), "pass"))
                elif symbolic.startswith("return "):
                    result_lines.append(generate_safe(struct.get("return", "return {}"), symbolic.split("return", 1)[-1].strip()))
                elif symbolic.startswith("comment "):
                    result_lines.append(generate_safe(struct.get("comment", "# {}"), symbolic.split("comment", 1)[-1].strip().strip('"')))
                else:
                    result_lines.append(comment.format("Unrecognized: " + symbolic))
            except Exception as e:
                result_lines.append(comment.format(f"Error: {e} in line: {symbolic}"))

        outputs[lang] = "\n".join(result_lines)

    return jsonify(outputs)

@app.route("/download")
def download():
    zip_path = os.path.join(OUTPUT_DIR, "usl_outputs.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for filename in os.listdir(OUTPUT_DIR):
            zipf.write(os.path.join(OUTPUT_DIR, filename), arcname=filename)
    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
