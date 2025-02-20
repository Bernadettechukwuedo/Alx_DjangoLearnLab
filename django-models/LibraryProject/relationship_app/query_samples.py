from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
author_name = "Bernadette Chukwuedo"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
for book in books:
    print(book)

# List all books in a library.
library_name = "National Library"
library = Library.objects.get(name=library_name)
books = library.books.all()
for book in books:
    print(book)

# Retrieve the librarian for a library.
library_name = "National Library"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(librarian)
