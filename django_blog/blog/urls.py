from django.urls import path, include
from .views import register, login_user, profile, logout_user
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
)

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", logout_user, name="logout"),
    path("post/", PostListView.as_view(), name="list_view"),
    path("post/new/", PostCreateView.as_view(), name="create_view"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detail_view"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="update_view"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="list_view"),
]
