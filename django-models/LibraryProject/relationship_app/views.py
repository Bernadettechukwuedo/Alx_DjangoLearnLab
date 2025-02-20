from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView


# List view.
def list_books(request):
    book = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": book})


class list_availabilityView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
