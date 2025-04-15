
import os

def detect_language_by_extension(filename):
    ext = os.path.splitext(filename)[-1].lower()
    ext_map = {
        ".py": "python",
        ".js": "javascript",
        ".c": "c",
        ".cpp": "cpp",
        ".java": "java",
        ".ts": "typescript"
    }
    return ext_map.get(ext, "unknown")

def reverse_parser(code_lines, language):
    symbolic_lines = []

    for line in code_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith(("//", "#")):
            continue

        l = stripped.lower()

        if "print" in l:
            symbolic_lines.append("Symbolic: print(" + stripped.split("(", 1)[-1].rsplit(")", 1)[0] + ")")
        elif "=" in l and "==" not in l:
            symbolic_lines.append("Symbolic: let " + stripped)
        elif l.startswith("def ") or "function" in l or l.startswith("fn "):
            func_part = stripped.split("(", 1)[0].split()[-1]
            args = stripped.split("(", 1)[-1].rsplit(")", 1)[0]
            symbolic_lines.append(f"Symbolic: function {func_part}({args})")
        elif "return " in l:
            symbolic_lines.append("Symbolic: return " + stripped.split("return", 1)[-1].strip())
        elif "if " in l:
            cond = stripped.split("if", 1)[-1].split(":")[0].strip("() {}:")
            symbolic_lines.append("Symbolic: if " + cond)
        elif "for " in l or "while" in l:
            symbolic_lines.append("Symbolic: loop " + stripped)
        elif "class " in l:
            symbolic_lines.append("Symbolic: class " + stripped.split("class", 1)[-1].strip())
        elif "switch" in l:
            symbolic_lines.append("Symbolic: switch " + stripped.split("switch", 1)[-1].strip())
        elif "import " in l:
            symbolic_lines.append("Symbolic: import " + stripped.split("import", 1)[-1].strip())
        elif "try" in l:
            symbolic_lines.append("Symbolic: try")
        elif "throw" in l:
            symbolic_lines.append("Symbolic: throw error")
        elif "continue" in l:
            symbolic_lines.append("Symbolic: continue")
        elif "break" in l:
            symbolic_lines.append("Symbolic: break")
        elif "await" in l:
            symbolic_lines.append("Symbolic: await result")
        elif "async" in l:
            symbolic_lines.append("Symbolic: async fetch(url)")
        elif "yield" in l:
            symbolic_lines.append("Symbolic: yield value")
        elif "+" in l or "-" in l or "*" in l or "/" in l:
            symbolic_lines.append("Symbolic: operator " + stripped)
        elif "namespace" in l:
            symbolic_lines.append("Symbolic: namespace " + stripped.split("namespace", 1)[-1].strip())
        elif "main" in l:
            symbolic_lines.append("Symbolic: main")
        else:
            symbolic_lines.append("// Could not parse: " + stripped)

    return symbolic_lines
