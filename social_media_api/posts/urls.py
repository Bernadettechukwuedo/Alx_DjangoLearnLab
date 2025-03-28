from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewset, CommentViewset, feed_posts, LikePostView,UnlikePostView

router = DefaultRouter()

router.register(r"posts", PostViewset, basename="post")
router.register(r"comments", CommentViewset, basename="comment")

# Include the router-generated URLs
urlpatterns = [
    path("", include(router.urls)),
    path("feed/", feed_posts, name="feed-posts"),
    path("posts/<int:pk>/like/", LikePostView.as_view(), name="like-post"),
    path("posts/<int:pk>/unlike/", UnlikePostView.as_view(), name="like-post")
]
