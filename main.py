from db import init_db
from models import (
    get_by_id,
    get_books_by_author
)
from cache import (
    get_cache,
    set_cache
)


def search_book_by_id():
    book_id = input("Book ID енгізіңіз: ")

    cache_key = f"book:{book_id}"

    cached = get_cache(cache_key)

    if cached:
        print("\nCACHE:")
        print(cached)
        return

    result = get_by_id(book_id)

    if result:
        data = (
            f"ID: {result[0]}, "
            f"Title: {result[1]}, "
            f"Author: {result[2]}"
        )

        set_cache(cache_key, data)

        print("\nDB:")
        print(data)

    else:
        print("Кітап табылмады")


def search_by_author():
    author = input("Автор аты: ")

    results = get_books_by_author(author)

    if not results:
        print("Кітап табылмады")
        return

    print("\nНәтижелер:")

    for book in results:
        print(
            f"Book: {book[0]} | "
            f"Author: {book[1]}"
        )


def menu():

    while True:

        print("\n===== BOOK LIBRARY SYSTEM =====")
        print("1. Book search by ID")
        print("2. Search by author")
        print("3. Exit")

        choice = input("Таңдау: ")

        if choice == "1":
            search_book_by_id()

        elif choice == "2":
            search_by_author()

        elif choice == "3":
            print("Бағдарлама аяқталды")
            break

        else:
            print("Қате таңдау")


if __name__ == "__main__":
    init_db()
    menu()