import ast

def check_python_syntax(code):
    try:
        ast.parse(code)
        return "✅ Syntax is correct!", None
    except SyntaxError as e:
        return f"❌ Syntax Error: {e.msg} at line {e.lineno}", e
