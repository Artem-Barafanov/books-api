from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Books API is running!"


@app.route("/books")
def get_books():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "books"),
        user=os.getenv("DB_USER", "student"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, title, author FROM books ORDER BY id")
        rows = cursor.fetchall()

        books = [
            {"id": row[0], "title": row[1], "author": row[2]}
            for row in rows
        ]

        return jsonify(books)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
