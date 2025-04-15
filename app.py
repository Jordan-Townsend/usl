
import os
import json
import zipfile
from flask import Flask, request, render_template_string, send_file
from reverse_parser import reverse_parser, detect_language_by_extension

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
                elif symbolic.startswith("Symbolic: return "):
                    value = symbolic.split("return", 1)[-1].strip()
                    f.write(generate_safe(struct.get("return", "return {}"), value) + "\n")
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
            ext_lang = detect_language_by_extension(file.filename)
            path = os.path.join(UPLOAD_DIR, file.filename)
            file.save(path)

            with open(path, "r") as f:
                lines = f.readlines()

            if not any(line.startswith("Symbolic:") for line in lines):
                reversed_usl = reverse_parser(lines, ext_lang)
                lines = [line + "\n" for line in reversed_usl]

            for lang in languages:
                available_keys = syntax[lang].get("structure", {}).keys()
                needed = [line.split()[1].split("(")[0] for line in lines if "Symbolic:" in line]
                if any(symbol in available_keys for symbol in needed):
                    transpile(lines, lang, syntax)

            build_zip()
            zip_ready = True

    return render_template_string("""
<html>
<head>
  <title>USL Web Converter</title>
  <script>
    function previewFile() {
      const fileInput = document.getElementById("fileInput");
      const preview = document.getElementById("preview");
      const file = fileInput.files[0];
      const reader = new FileReader();
      reader.onload = function(e) {
        preview.value = e.target.result;
      };
      reader.readAsText(file);
    }
  </script>
</head>
<body>
  <h2>USL Converter – Upload .usl or Code File</h2>
  <form method="post" enctype="multipart/form-data">
    <input type="file" id="fileInput" name="file" onchange="previewFile()" required><br><br>
    <textarea id="preview" style="width:100%;height:200px" readonly placeholder="Uploaded code preview..."></textarea><br><br>
    <input type="submit" value="Convert">
  </form>
  {% if zip_ready %}
  <h3><a href="/download_all">Download All Outputs (ZIP)</a></h3>
  {% endif %}
</body>
</html>
""", zip_ready=zip_ready, languages=languages)

@app.route("/download_all")
def download_all():
    return send_file(os.path.join(OUTPUT_DIR, "all_outputs.zip"), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
