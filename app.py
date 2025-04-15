
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
                    assign_expr = symbolic.split("let ", 1)[-1]
                    left, right = assign_expr.split("=")
                    f.write(generate_safe(struct.get("assign", "{} = {}"), left.strip(), right.strip()) + "\n")
                elif symbolic.startswith("Symbolic: if "):
                    condition = symbolic[13:]
                    f.write(generate_safe(struct.get("if", "if {}:\n    {}"), condition.strip(), "print('true')") + "\n")
                elif symbolic.startswith("Symbolic: function "):
                    header = symbolic.split("function", 1)[-1].strip()
                    name, rest = header.split("(", 1)
                    args = rest.split(")")[0]
                    f.write(generate_safe(struct.get("function", "def {}({}):\n    {}"), name.strip(), args.strip(), "print(name)") + "\n")
                elif symbolic.startswith("Symbolic: loop"):
                    loop_expr = symbolic.split("loop", 1)[-1].strip()
                    f.write(generate_safe(struct.get("loop", "for i in range({}):\n  {}"), loop_expr, "pass") + "\n")
                elif symbolic.startswith("Symbolic: comment"):
                    comment_text = symbolic.split("comment", 1)[-1].strip().strip('"')
                    f.write(generate_safe(struct.get("comment", "# {}"), comment_text) + "\n")
                elif symbolic.startswith("Symbolic: class "):
                    class_expr = symbolic.split("class", 1)[-1].strip()
                    name, args = class_expr.split("(", 1)
                    args = args.strip(")")
                    f.write(generate_safe(struct.get("class", "class {}({}):\n    def __init__(self):\n        {}"), name.strip(), args.strip(), "pass") + "\n")
                elif symbolic.startswith("Symbolic: switch"):
                    f.write(generate_safe(struct.get("switch", "switch({}) {{ case ... }}"), "x") + "\n")
                elif symbolic.startswith("Symbolic: import "):
                    imp = symbolic.split("import", 1)[-1].strip()
                    f.write(generate_safe(struct.get("import", "import {}"), imp) + "\n")
                elif symbolic.startswith("Symbolic: return "):
                    value = symbolic.split("return", 1)[-1].strip()
                    f.write(generate_safe(struct.get("return", "return {}"), value) + "\n")
                elif symbolic.startswith("Symbolic: try"):
                    f.write(generate_safe(struct.get("try", "try {{ {} }} catch {{ {} }}"), "attempt", "handle") + "\n")
                elif symbolic.startswith("Symbolic: break"):
                    f.write(generate_safe(struct.get("break", "break")) + "\n")
                elif symbolic.startswith("Symbolic: continue"):
                    f.write(generate_safe(struct.get("continue", "continue")) + "\n")
                elif symbolic.startswith("Symbolic: else"):
                    f.write(generate_safe(struct.get("else", "else:\n    {}"), "print('else')") + "\n")
                elif symbolic.startswith("Symbolic: elif "):
                    cond = symbolic.split("elif", 1)[-1].strip()
                    f.write(generate_safe(struct.get("elif", "elif {}:\n    {}"), cond, "print('elif')") + "\n")
                elif symbolic.startswith("Symbolic: while "):
                    condition = symbolic.split("while", 1)[-1].strip()
                    f.write(generate_safe(struct.get("while", "while {}:\n    {}"), condition, "pass") + "\n")
                elif symbolic.startswith("Symbolic: throw"):
                    f.write(generate_safe(struct.get("throw", "throw {}"), "Error") + "\n")
                elif symbolic.startswith("Symbolic: async"):
                    f.write(generate_safe(struct.get("async", "async function {}({}) {{ {} }}"), "fetch", "url", "await fetch(url)") + "\n")
                elif symbolic.startswith("Symbolic: await"):
                    f.write(generate_safe(struct.get("await", "await {}"), "result") + "\n")
                elif symbolic.startswith("Symbolic: yield"):
                    f.write(generate_safe(struct.get("yield", "yield {}"), "value") + "\n")
                elif symbolic.startswith("Symbolic: operator"):
                    f.write(generate_safe(struct.get("operator", "{} + {}"), "a", "b") + "\n")
                elif symbolic.startswith("Symbolic: namespace"):
                    f.write(generate_safe(struct.get("namespace", "namespace {} {{ {} }}"), "myApp", "// logic") + "\n")
                elif symbolic.startswith("Symbolic: main"):
                    f.write(generate_safe(struct.get("main", "int main() {{ {} }}"), "return 0;") + "\n")
                else:
                    f.write(comment.format("Unrecognized: " + symbolic) + "\n")
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
            for lang in languages:
                transpile(lines, lang, syntax)
            build_zip()
            zip_ready = True

    return render_template_string("""<html><head><title>USL Hosted App</title></head>
<body>
<h2>Upload a USL File and Transpile to All 111 Languages</h2>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="file" required><br><br>
  <input type="submit" value="Transpile">
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
