from django.urls import path, include
from .views import register, login_user, profile, logout_user
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    CommentCreateView,
    CommentListView,
    CommentUpdateView,
    CommentDeleteView,
    PostByTagListView,
    posts_by_tag,
    search_results,
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
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete_view"),
    path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="create_comment",
    ),
    path(
        "posts/<int:post_id>/comments", CommentListView.as_view(), name="list_comment"
    ),
    path(
        "comment/<int:pk>/update/",
        CommentUpdateView.as_view(),
        name="update_comment",
    ),
    path(
        "comment/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="delete_comment",
    ),
    path(
        "search/",
        search_results,
        name="search_results",
    ),
    path("tags/<str:tag_name>/", posts_by_tag, name="posts-by-tag"),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"),
]
