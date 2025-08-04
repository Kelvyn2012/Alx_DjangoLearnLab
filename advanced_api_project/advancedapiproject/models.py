from django.db import models


# The Author model stores information about a book author.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's full name

    def __str__(self):
        return self.name


# The Book model represents a book written by an Author.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.PositiveIntegerField()  # Year the book was published
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    # The ForeignKey establishes a one-to-many relationship: one author can have many books.

    def __str__(self):
        return self.title
