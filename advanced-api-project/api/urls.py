from django.urls import path, include
from .views import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("books/", ListView.as_view(), name="book-list"),
    path("books/<int:pk>", DetailView.as_view(), name="book-detail"),
    path("books/create/", CreateView.as_view(), name="book-create"),
    path("books/update/<int:pk>", UpdateView.as_view(), name="book-update"),
    path("books/delete/<int:pk>", DeleteView.as_view(), name="book-delete"),
    path("api/token/", obtain_auth_token, name="api_token_auth"),
]
