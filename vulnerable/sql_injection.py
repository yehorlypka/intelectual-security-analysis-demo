import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def find_user():
    username = request.args.get("username", "")

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Intentionally vulnerable code.
    query = (
        "SELECT * FROM users "
        "WHERE username = '" + username + "'"
    )

    cursor.execute(query)

    return {"users": cursor.fetchall()}