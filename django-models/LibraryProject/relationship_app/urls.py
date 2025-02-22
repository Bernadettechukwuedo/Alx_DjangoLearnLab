from django.urls import path, include
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="list_details"),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
    path("admin_view/", views.admin_view, name="admin"),
    path("librarian/", views.librarian_view, name="librarian"),
    path("member/", views.member_view, name="member"),
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/", views.edit_book, name="change_book"),
    path("delete_book/", views.delete_book, name="delete_book"),
]
