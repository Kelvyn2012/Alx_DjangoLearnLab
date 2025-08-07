from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.author = Author.objects.create(name="Andrew Hunt")

        self.book1 = Book.objects.create(
            title="The Pragmatic Programmer", publication_year=1999, author=self.author
        )
        self.book2 = Book.objects.create(
            title="Clean Code", publication_year=2008, author=self.author
        )
        self.book3 = Book.objects.create(
            title="The Clean Coder", publication_year=2011, author=self.author
        )

    def test_book_list_authenticated(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_book_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        url = reverse("book-create")
        data = {
            "title": "Refactoring",
            "publication_year": 2000,
            "author": self.author.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse("book-create")
        data = {
            "title": "Refactoring",
            "publication_year": 2000,
            "author": self.author.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 2001,
            "author": self.author.id,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books_by_title(self):
        url = reverse("book-list")
        response = self.client.get(url, {"title": "Clean Code"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Clean Code")

    def test_search_books_by_title(self):
        url = reverse("book-list")
        response = self.client.get(url, {"search": "Clean"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertIn("Clean Code", titles)
        self.assertIn("The Clean Coder", titles)

    def test_order_books_by_year_descending(self):
        url = reverse("book-list")
        response = self.client.get(url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
