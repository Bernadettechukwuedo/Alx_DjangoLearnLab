from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
books = Book.objects.filter(author__name="J.K. Rowling")
for book in books:
    print(book)

# List all books in a library.
library_name = "National Library"
library = Library.objects.get(name=library_name)
books = library.books.all()
for book in books:
    print(book)

# Retrieve the librarian for a library.
librarian = Librarian.objects.get(library__name=library_name)
print(librarian)
