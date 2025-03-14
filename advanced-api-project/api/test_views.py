from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status

# Create your tests here.

""" 
A unit test to test for the following CRUD operation :creation of a book, the test is successful if the status code is 201, updating a specific book, the test is successful if the 
status code is 200, deleting a specific book, the test is successful if the status code is 204. It includes test cases for unsuccessful CRUD operations
(i.e the CRUD operations thst requires authentication)


To run the test use python manage.py test api

"""


class BookTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.title = "leadership"
        self.publication_year = 2022
        self.author = Author.objects.create(name="John Doe")
        self.author_id = self.author.id
        self.book = Book.objects.create(
            title=self.title, publication_year=self.publication_year, author=self.author
        )
        self.book_id = self.book.id

    def test_successful_creation(self):
        payload = {
            "title": self.title,
            "publication_year": self.publication_year,
            "author": self.author_id,
        }
        response = self.client.post("/books/create/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("title", response.data)
        self.assertIn("publication_year", response.data)
        self.assertIn("author", response.data)

    def test_succcessful_update_book(self):
        payload = {
            "title": self.title,
            "publication_year": self.publication_year,
            "author": self.author_id,
        }
        response = self.client.put(
            f"/books/update/{self.book_id}", payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", response.data)
        self.assertIn("title", response.data)
        self.assertIn("publication_year", response.data)
        self.assertIn("author", response.data)

    def test_successful_delete_book(self):
        payload = {
            "title": self.title,
            "publication_year": self.publication_year,
            "author": self.author_id,
        }
        response = self.client.delete(
            f"/books/delete/{self.book_id}", payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_book(self):
        self.client.credentials()
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unsuccessful_creation(self):
        self.client.credentials()
        payload = {
            "title": self.title,
            "publication_year": self.publication_year,
            "author": self.author_id,
        }
        response = self.client.post("/books/create/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unsucccessful_update_book(self):
        self.client.credentials()
        payload = {
            "title": self.title,
            "publication_year": self.publication_year,
            "author": self.author_id,
        }
        response = self.client.put(
            f"/books/update/{self.book_id}", payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_successful_delete_book(self):
        self.client.credentials()
        payload = {
            "title": self.title,
            "publication_year": self.publication_year,
            "author": self.author_id,
        }
        response = self.client.delete(
            f"/books/delete/{self.book_id}", payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
