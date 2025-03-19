from django.urls import path, include
from .views import register, login_user, profile, logout_user
from .views import ListView, DetailView, UpdateView, DeleteView, CreateView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", logout_user, name="logout"),
    path("posts/", ListView.as_view(), name="list_view"),
    path("posts/new/", CreateView.as_view(), name="create_view"),
    path("posts/<int:pk>/", DetailView.as_view(), name="detail_view"),
    path("posts/<int:pk>/edit/", UpdateView.as_view(), name="update_view"),
    path("posts/<int:pk>/delete/", DeleteView.as_view(), name="delete_view"),
]
