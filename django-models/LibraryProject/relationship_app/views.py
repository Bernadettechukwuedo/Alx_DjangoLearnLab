from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse


# List view.
def list_books(request):
    book = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": book})


# list details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "relationship_app/register.html", {"form": form})


def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return redirect("login")
    return render(request, "relationship_app/login.html")


def is_Admin(user):
    return (
        user.is_authenticated
        and hasattr(user, "userprofile")
        and user.userprofile.role == "Admin"
    )


def is_Librarian(user):
    return (
        user.is_authenticated
        and hasattr(user, "userprofile")
        and user.userprofile.role == "Librarian"
    )


def is_Member(user):
    return (
        user.is_authenticated
        and hasattr(user, "userprofile")
        and user.userprofile.role == "Member"
    )


@login_required
@user_passes_test(is_Admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html", {"role": "Admin"})


@login_required
@user_passes_test(is_Librarian)
def librarian_view(request):
    return render(
        request, "relationship_app/librarian_view.html", {"role": "Librarian"}
    )


@login_required
@user_passes_test(is_Member)
def member_view(request):
    return render(request, "relationship_app/member_view.html", {"role": "Member"})


@permission_required("relationship_app.can_add_book")
def add_book(request):
    pass


@permission_required("relationship_app.can_change_book")
def edit_book(request):
    pass


@permission_required("relationship_app.can_delete_book")
def delete_book(request):
    pass
