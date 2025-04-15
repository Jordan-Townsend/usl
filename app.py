
import os, json, zipfile
from flask import Flask, request, render_template_string, send_file

app = Flask(__name__)
UPLOAD_DIR = "usl_web_uploads"
OUTPUT_DIR = "usl_outputs"
SYNTAX_FILE = "syntax_templates_verified_real_final.json"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_usl_lines(lines, target_lang):
    matched = []
    fallback = []
    for line in lines:
        line = line.strip()
        if line.startswith(f"Symbolic[{target_lang}]"):
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
    struct = syntax[lang]["structure"]
    comment = struct.get("comment", "# {}")
    ext = syntax[lang]["file_extensions"][0]
    filename = f"{lang}.{ext}"
    output_path = os.path.join(OUTPUT_DIR, filename)
    parsed = parse_usl_lines(lines, lang)

    with open(output_path, "w") as f:
        f.write(comment.format(f"This is {lang} syntax") + "\n")
        for symbolic in parsed:
            try:
                if "print(" in symbolic:
                    value = symbolic.split("print(", 1)[1].split(")", 1)[0]
                    f.write(generate_safe(struct.get("print", "{}"), value) + "\n")
                elif "let " in symbolic:
                    assign = symbolic.split("let ", 1)[1]
                    left, right = assign.split("=")
                    f.write(generate_safe(struct.get("assign", "{} = {}"), left.strip(), right.strip()) + "\n")
                elif symbolic.startswith("if "):
                    condition = symbolic[3:]
                    f.write(generate_safe(struct.get("if", "if {}:\n    {}"), condition.strip(), "pass") + "\n")
                elif symbolic.startswith("function "):
                    head = symbolic.split("function", 1)[-1].strip()
                    name, args = head.split("(", 1)
                    args = args.rstrip(")")
                    f.write(generate_safe(struct.get("function", "def {}({}):\n    {}"), name.strip(), args.strip(), "pass") + "\n")
                elif symbolic.startswith("return "):
                    f.write(generate_safe(struct.get("return", "return {}"), symbolic.split("return", 1)[-1].strip()) + "\n")
                elif symbolic.startswith("comment "):
                    f.write(generate_safe(struct.get("comment", "# {}"), symbolic.split("comment", 1)[-1].strip().strip('"')) + "\n")
                else:
                    f.write(comment.format("Unrecognized: " + symbolic) + "\n")
            except Exception as e:
                f.write(comment.format(f"Error: {e} in line: {symbolic}") + "\n")
    return filename

def build_zip():
    zip_path = os.path.join(OUTPUT_DIR, "all_outputs.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for f in os.listdir(OUTPUT_DIR):
            if not f.endswith(".zip"):
                zipf.write(os.path.join(OUTPUT_DIR, f), arcname=f)
    return zip_path

@app.route("/", methods=["GET", "POST"])
def index():
    zip_ready = False
    languages = []
    if os.path.exists(SYNTAX_FILE):
        with open(SYNTAX_FILE, "r") as f:
            syntax = json.load(f)
            languages = ["usl"] + sorted(syntax.keys())
    if request.method == "POST":
        file = request.files.get("file")
        if file:
            path = os.path.join(UPLOAD_DIR, file.filename)
            file.save(path)
            with open(path, "r") as f:
                lines = f.readlines()
            selected = request.form.getlist("languages")
            for lang in selected:
                if lang == "usl":
                    with open(os.path.join(OUTPUT_DIR, "usl_input_original.usl"), "w") as f_out:
                        f_out.writelines(lines)
                    continue
                transpile(lines, lang, syntax)
            build_zip()
            zip_ready = True

    return render_template_string("""
    <html><head><title>USL App</title></head>
    <body>
    <h2>Upload a .usl file and select target language(s)</h2>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file" required><br><br>
      <label>Select one or more languages:</label><br>
      <select name="languages" multiple size="15" required>
        <option value="usl">USL (original)</option>
        {% for lang in languages %}
          <option value="{{ lang }}">{{ lang }}</option>
        {% endfor %}
      </select><br>
      <input type="submit" value="Transpile">
    </form>
    {% if zip_ready %}
      <h3><a href="/download_all">📦 Download ZIP</a></h3>
    {% endif %}
    </body></html>
    """, zip_ready=zip_ready, languages=languages)

@app.route("/download_all")
def download_all():
    return send_file(os.path.join(OUTPUT_DIR, "all_outputs.zip"), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=10000)
