import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute")
def execute_command():
    command = request.args.get("command", "")

    # Intentionally vulnerable code.
    subprocess.run(
        command,
        shell=True
    )

    return {"status": "executed"}