import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute")
def execute_command():
    user_argument = request.args.get("argument", "")

    subprocess.run(
        ["echo", user_argument],
        shell=False,
        check=True
    )

    return {"status": "executed"}