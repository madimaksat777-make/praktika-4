from db import get_connection


def get_by_id(book_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        books.id,
        books.title,
        authors.name
    FROM books
    JOIN authors
        ON books.author_id = authors.id
    WHERE books.id = ?
    """, (book_id,))

    result = cursor.fetchone()

    conn.close()

    return result


def get_books_by_author(author_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        books.title,
        authors.name
    FROM books
    JOIN authors
        ON books.author_id = authors.id
    WHERE authors.name LIKE ?
    """, (f"%{author_name}%",))

    results = cursor.fetchall()

    conn.close()

    return results