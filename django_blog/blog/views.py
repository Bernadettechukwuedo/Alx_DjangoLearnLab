from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, Post
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import BlogSerializer
from .models import Post


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


class ListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class DetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class CreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    template_name = "blog/CreateView.html"
    permission_classes = [permissions.IsAuthenticated]


class UpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
