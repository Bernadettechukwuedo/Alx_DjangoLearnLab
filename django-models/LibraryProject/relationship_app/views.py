from django.shortcuts import render
from .models import Book, Author, Library, Librarian
from django.views.generic import ListView, DetailView


# Create your views here.
def list_books(request):
    book = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": book})


class list_availabilityView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
