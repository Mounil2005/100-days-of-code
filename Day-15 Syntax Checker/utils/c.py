import subprocess
import tempfile
import os

def check_c_syntax(code):
    with tempfile.NamedTemporaryFile(mode='w', suffix='.c', delete=False) as tmp:
        tmp.write(code)
        tmp_filename = tmp.name

    result = subprocess.run(
        ['gcc', '-fsyntax-only', tmp_filename],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    os.unlink(tmp_filename)  # clean up

    if result.returncode == 0:
        return "✅ Syntax is correct!"
    else:
        return f"❌ Syntax Error:\n{result.stderr}"
