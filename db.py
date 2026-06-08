import sqlite3
from config import DB_NAME


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY(author_id) REFERENCES authors(id)
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM authors")
    count = cursor.fetchone()[0]

    if count == 0:

        cursor.execute(
            "INSERT INTO authors(name) VALUES (?)",
            ("Mukhtar Auezov",)
        )

        cursor.execute(
            "INSERT INTO authors(name) VALUES (?)",
            ("Ilyas Esenberlin",)
        )

        cursor.execute(
            "INSERT INTO books(title, author_id) VALUES (?, ?)",
            ("Abai Zholy", 1)
        )

        cursor.execute(
            "INSERT INTO books(title, author_id) VALUES (?, ?)",
            ("Koshpendiler", 2)
        )

        cursor.execute(
            "INSERT INTO books(title, author_id) VALUES (?, ?)",
            ("Kaharman", 2)
        )

    conn.commit()
    conn.close()