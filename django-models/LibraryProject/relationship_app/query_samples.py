import os
import django
from .models import Book, Librarian, Library, Author

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")


def books_by_author(author_name):
    try:
        author = Book.objects.all(name=author_name)
        books = author.books.all()
        print(f"Books by {author.name}:")
        for book in books:
            print(f"-{book.title}")
    except Author.DoesNotExist:
        print("Author not found.")


def books_in_library(library_name):
    try:
        library = Library.objects.all(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name}:")
        for book in books:
            print(f"-{book.title}")
    except Library.DoesNotExist:
        print("Library not found.")


def librarian_of_library(librarian_name):
    try:
        library = Library.objects.get(name=librarian_name)
        librarian = library.librarian
        print(f"Librarian of {library.name}: {librarian.name}")
    except (Librarian.DoesNotExist, Library.DoesNotExist):
        print("Library or Librarian not found.")
