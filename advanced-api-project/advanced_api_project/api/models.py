from django.db import models

# Create your models here.

# The Author model creates a table in the database called Author with the field called name


class Author(models.Model):
    name = models.CharField(max_length=100)


# The Book model creates a table in the database called Book with the fields called title, publication_year, and author(which is a foreign key to the author's table)


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
