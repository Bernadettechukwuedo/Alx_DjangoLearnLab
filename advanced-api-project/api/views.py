from django.shortcuts import render
from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
"""
A token based authentication is used and configured in the settings.py file 


"""


# This view, lists all the books and it is read only for unautenticated users
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # This view allows filtering based on the fields in the book model. it consists of search and order filter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "publication_year", "author"]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author__id"]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["title__icontains", "publication_year", "author"]


# This view, lists specific books based on the book id parsed and it is read only for unautenticated users


class DetailView(generics.RetrieveAPIView):

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Book.objects.all()
        book_id = self.request.query_params.get("id", None)
        if book_id is not None:
            queryset = queryset.filter(id=book_id)
        return queryset


# It creates new books and a user must be authenticated
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# It updates already existing  books and a user must be authenticated
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# deletes a specific book and the user must be authenticated
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
