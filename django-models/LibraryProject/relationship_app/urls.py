from django.urls import path, include
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="list_details"),
]
