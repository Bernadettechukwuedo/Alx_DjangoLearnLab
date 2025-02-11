from bookshelf.models import Book
books = Book.objects.get(title="Nineteen Eighty-Four") 
books.delete()
Book.objects.all()

<!-- <QuerySet []>-->