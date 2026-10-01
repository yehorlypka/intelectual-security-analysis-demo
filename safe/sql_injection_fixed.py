import sqlite3

def find_user():
    username = input("Enter username: ")

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    query = (
        "SELECT * FROM users "
        "WHERE username = ?"
    )

    cursor.execute(query, (username,))

    return cursor.fetchall()

if __name__ == "__main__":
    find_user()