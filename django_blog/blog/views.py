from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, PostForm
from django.contrib.auth.models import User
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post

"""
Blog Application Views:

- `profile(request)`: Displays the profile page. Redirects unauthenticated users to the login page.
- `register(request)`: Handles user registration. Ensures passwords match and checks for existing users before creating a new account.
- `login_user(request)`: Handles user login. Authenticates credentials and redirects users accordingly.
- `logout_user(request)`: Logs out the current user and redirects them to the login page.
- `PostListView`: Displays a list of all blog posts.
- `PostDetailView`: Displays details of a single blog post.
- `PostCreateView`: Allows authenticated users to create new blog posts.
- `PostUpdateView`: Allows the post author to edit their blog post.
- `PostDeleteView`: Allows the post author to delete their blog post.

Permissions:
- Only authenticated users can create a post.
- Only the author of a post can update or delete it.

Redirects:
- Successful registration redirects to login.
- Successful login redirects to the profile page.
- Successful post creation, update, or deletion redirects to the post list.

Templates:
- `blog/post_list.html`: Displays all posts.
- `blog/post_detail.html`: Displays a single post.
- `blog/post_form.html`: Form for creating a post.
- `blog/post_update.html`: Form for updating a post.
- `blog/post_delete.html`: Confirmation page for deleting a post.
"""


# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        redirect("login")

    return render(request, "blog/base.html", {"username": request.user.username})


def register(request):
    form = SignUpForm()
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1 != password2:
            return HttpResponse("Password do not match")

        if User.objects.filter(username=username).exists():
            print("user already exists")
            return render(request, "blog/register.html", {"form": form})
        try:
            user = User.objects.create_user(
                username=username, password=password1, email=email
            )
            user.save()
            return redirect("login")
        except Exception as e:
            print(f"Error creating {str(e)}")

    return render(request, "blog/register.html", {"form": form})


def login_user(request):
    form = SignUpForm()
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            return HttpResponse("Password do not match")
        user = authenticate(
            request,
            username=username,
            password=password1,
        )
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            print(f"{username} is not a registered user")
            return redirect("register")

    return render(request, "blog/login.html", {"form": form})


def logout_user(request):
    logout(request)
    print("logged out successfully")
    return redirect("login")


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("list_view")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("list_view")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("list_view")
    context_object_name = "posts"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
