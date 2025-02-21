from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
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
    if hasattr(user, "userprofile"):
        return user.userprofile.role == "Admin"
    return False


@user_passes_test(is_Admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")


def is_Librarian(user):
    if hasattr(user, "userprofile"):
        return user.userprofile.role == "Librarian"
    return False


@user_passes_test(is_Librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")


def is_Member(user):
    if hasattr(user, "userprofile"):
        return user.userprofile.role == "Member"
    return False


@user_passes_test(is_Member)
def member_view(request):
    return HttpResponse("Welcome, Member!")
