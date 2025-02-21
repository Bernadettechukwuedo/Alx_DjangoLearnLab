from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(
        Library, related_name="librarians", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


role_choices = [("Admin", "Admin"), ("Librarian", "Librarian"), ("Member", "Member")]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=role_choices, max_length=255, default="Member")

    def __str__(self):
        return f"{self.user.username} - {self.role}"
