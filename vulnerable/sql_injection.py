import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def find_user():
    username = request.args.get("username", "")

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Parameterized query prevents SQL injection.
    query = (
        "SELECT * FROM users "
        "WHERE username = ?"
    )

    cursor.execute(query, (username,))

    return {"users": cursor.fetchall()}