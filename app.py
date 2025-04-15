
import os
import json
import zipfile
from flask import Flask, request, render_template_string, send_file

app = Flask(__name__)
UPLOAD_DIR = "usl_web_uploads"
OUTPUT_DIR = "usl_outputs"
SYNTAX_FILE = "syntax_templates_verified_real_final.json"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_usl_lines(lines):
    return [line.strip() for line in lines if line.strip().startswith("Symbolic:")]

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
    parsed = parse_usl_lines(lines)

    with open(output_path, "w") as f:
        f.write(comment.format(f"This is {lang} syntax") + "\n")
        for line in parsed:
            symbolic = line.strip()
            try:
                if symbolic.startswith("Symbolic: print("):
                    value = symbolic.split("print(", 1)[1].rsplit(")", 1)[0]
                    f.write(generate_safe(struct.get("print", "{}"), value) + "\n")
                elif symbolic.startswith("Symbolic: let "):
                    expr = symbolic.split("let ", 1)[-1]
                    left, right = expr.split("=")
                    f.write(generate_safe(struct.get("assign", "{} = {}"), left.strip(), right.strip()) + "\n")
                elif symbolic.startswith("Symbolic: function "):
                    header = symbolic.split("function", 1)[-1].strip()
                    name, rest = header.split("(", 1)
                    args = rest.split(")")[0]
                    f.write(generate_safe(struct.get("function", "def {}({}):\n    {}"), name.strip(), args.strip(), "pass") + "\n")
                elif symbolic.startswith("Symbolic: if "):
                    cond = symbolic.split("if ", 1)[-1].strip()
                    f.write(generate_safe(struct.get("if", "if {}:\n    {}"), cond, "pass") + "\n")
                elif symbolic.startswith("Symbolic: elif "):
                    cond = symbolic.split("elif ", 1)[-1].strip()
                    f.write(generate_safe(struct.get("elif", "elif {}:\n    {}"), cond, "pass") + "\n")
                elif symbolic.startswith("Symbolic: else"):
                    f.write(generate_safe(struct.get("else", "else:\n    {}"), "pass") + "\n")
                elif symbolic.startswith("Symbolic: loop "):
                    expr = symbolic.split("loop ", 1)[-1].strip()
                    f.write(generate_safe(struct.get("loop", "for i in range({}):\n  {}"), expr, "pass") + "\n")
                elif symbolic.startswith("Symbolic: while "):
                    cond = symbolic.split("while ", 1)[-1].strip()
                    f.write(generate_safe(struct.get("while", "while {}:\n    {}"), cond, "pass") + "\n")
                elif symbolic.startswith("Symbolic: return "):
                    value = symbolic.split("return", 1)[-1].strip()
                    f.write(generate_safe(struct.get("return", "return {}"), value) + "\n")
                elif symbolic.startswith("Symbolic: throw "):
                    value = symbolic.split("throw", 1)[-1].strip()
                    f.write(generate_safe(struct.get("throw", "throw {}"), value) + "\n")
                elif symbolic.startswith("Symbolic: yield"):
                    value = symbolic.split("yield", 1)[-1].strip() or "value"
                    f.write(generate_safe(struct.get("yield", "yield {}"), value) + "\n")
                elif symbolic.startswith("Symbolic: await "):
                    val = symbolic.split("await ", 1)[-1].strip()
                    f.write(generate_safe(struct.get("await", "await {}"), val) + "\n")
                elif symbolic.startswith("Symbolic: async"):
                    f.write(generate_safe(struct.get("async", "async function {}({}) {{ {} }}"), "fetch", "url", "await fetch(url)") + "\n")
                elif symbolic.startswith("Symbolic: try"):
                    f.write(generate_safe(struct.get("try", "try {{ {} }} catch {{ {} }}"), "attempt", "handle") + "\n")
                elif symbolic.startswith("Symbolic: break"):
                    f.write(generate_safe(struct.get("break", "break")) + "\n")
                elif symbolic.startswith("Symbolic: continue"):
                    f.write(generate_safe(struct.get("continue", "continue")) + "\n")
                elif symbolic.startswith("Symbolic: comment"):
                    text = symbolic.split("comment", 1)[-1].strip().strip('"')
                    f.write(generate_safe(struct.get("comment", "# {}"), text) + "\n")
                elif symbolic.startswith("Symbolic: import "):
                    val = symbolic.split("import", 1)[-1].strip()
                    f.write(generate_safe(struct.get("import", "import {}"), val) + "\n")
                elif symbolic.startswith("Symbolic: switch "):
                    val = symbolic.split("switch", 1)[-1].strip()
                    f.write(generate_safe(struct.get("switch", "switch({})"), val) + "\n")
                elif symbolic.startswith("Symbolic: class "):
                    header = symbolic.split("class", 1)[-1].strip()
                    name, rest = header.split("(", 1)
                    args = rest.split(")")[0]
                    f.write(generate_safe(struct.get("class", "class {}({}):\n    def __init__(self):\n        {}"), name.strip(), args.strip(), "pass") + "\n")
                elif symbolic.startswith("Symbolic: operator "):
                    expr = symbolic.split("operator", 1)[-1].strip()
                    f.write(generate_safe(struct.get("operator", "{}"), expr) + "\n")
                elif symbolic.startswith("Symbolic: namespace "):
                    ns = symbolic.split("namespace", 1)[-1].strip()
                    f.write(generate_safe(struct.get("namespace", "namespace {} {{ {} }}"), ns, "// logic") + "\n")
                elif symbolic.startswith("Symbolic: main"):
                    f.write(generate_safe(struct.get("main", "int main() {{ {} }}"), "return 0;") + "\n")
                else:
                    f.write(comment.format("Unparsed: " + symbolic) + "\n")
            except Exception as e:
                f.write(comment.format(f"Error: {str(e)} in line: {symbolic}") + "\n")
    return filename

def build_zip():
    zip_path = os.path.join(OUTPUT_DIR, "all_outputs.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in os.listdir(OUTPUT_DIR):
            if file.endswith(".zip"): continue
            zipf.write(os.path.join(OUTPUT_DIR, file), arcname=file)
    return zip_path

@app.route("/", methods=["GET", "POST"])
def index():
    zip_ready = False
    languages = []

    if os.path.exists(SYNTAX_FILE):
        with open(SYNTAX_FILE, "r") as f:
            syntax = json.load(f)
            languages = sorted(syntax.keys())
    else:
        return "Syntax file missing."

    if request.method == "POST":
        file = request.files.get("file")
        if file:
            path = os.path.join(UPLOAD_DIR, file.filename)
            file.save(path)
            with open(path, "r") as f:
                lines = f.readlines()
            selected_langs = request.form.getlist("languages")
            for lang in selected_langs:
                if lang == "usl":
                    with open(os.path.join(OUTPUT_DIR, "usl_input_original.usl"), "w") as f_out:
                        f_out.writelines(lines)
                    continue
                transpile(lines, lang, syntax)
                transpile(lines, lang, syntax)
            build_zip()
            zip_ready = True

    return render_template_string("""<html><head><title>USL Hosted App</title></head>
<body>
<h2>Upload a USL File and Transpile to All 111 Languages</h2>
<form method="post" enctype="multipart/form-data">
  <label>Select one or more languages:</label><br>
  <select id="language-select" name="languages" multiple size="15" required>
    <option value="usl">USL (original)</option>

    <option value="usl">USL (original)</option>
    {% for lang in languages %}
      <option value="{{ lang }}">{{ lang }}</option>
    {% endfor %}
  </select><br><br>
  <input type="file" name="file" required><br><br>
  <p style="font-size:0.9em;color:gray;">(Hold Ctrl or Cmd to select more than one)</p>
  <button type="button" onclick="selectAll()">Select All</button><br><br>
  <input type="submit" value="Transpile">
  <script>
    function selectAll() {
      var select = document.getElementById("language-select");
      for (var i = 0; i < select.options.length; i++) {
        select.options[i].selected = true;
      }
    }
  </script>
</form>
{% if zip_ready %}
<h3><a href="/download_all">📦 Download All Outputs (ZIP)</a></h3>
{% endif %}
</body></html>
""", zip_ready=zip_ready, languages=languages)

@app.route("/download_all")
def download_all():
    return send_file(os.path.join(OUTPUT_DIR, "all_outputs.zip"), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
