from django.shortcuts import render
from .serializers import PostSerializer, CommentSerializer, FeedPostSerializer
from rest_framework import viewsets
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions, status, generics
from rest_framework import serializers, filters, response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from .models import Like, Post
from notifications.models import Notification

# Create your views here.
"""
Django's built-in ViewSet is used to perform CRUD operations. Here, only the user who created a post can update or delete it, as enforced through permissions, which are defined in the permissions file. The same restriction applies to comments.

Pagination is enabled using Django's built-in pagination, which is configured by default in the settings file.

### Endpoints for Posts using ViewSet:
- `POST /api/posts/` → Create a new post
- `GET /api/posts/` → Retrieve all posts
- `GET /api/posts/{id}/` → Retrieve a single post by ID
- `PATCH /api/posts/{id}/` → Partially update a post
- `DELETE /api/posts/{id}/` → Delete a post (only by the creator)
- `PUT /api/posts/{id}/` → Update a post (only by the creator)

### Endpoints for Comments using ViewSet:
- `POST /api/comments/` → Create a new comment
- `GET /api/comments/` → Retrieve all comments
- `GET /api/comments/{id}/` → Retrieve a single comment by ID
- `PUT /api/comments/{id}/` → Update a comment (only by the creator)
- `PATCH /api/comments/{id}/` → Partially update a comment
- `DELETE /api/comments/{id}/` → Delete a comment (only by the creator)

### Filtering and Searching:
Users can filter posts based on keywords, full titles, or content using the search feature.
- Example: `GET /posts/posts/?search=Computer`
"""


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "content"]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    @action(
        detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated]
    )
    def feed(self, request):

        following_users = request.user.following.all()
        queryset = Post.objects.filter(author__in=following_users).order_by(
            "-created_at"
        )

        # Paginate results
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = FeedPostSerializer(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(serializer.data)

        serializer = FeedPostSerializer(
            queryset, many=True, context={"request": request}
        )
        return response.Response(serializer.data)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.request.data.get("post")  # Get post ID from request data
        if not post_id:
            raise serializers.ValidationError({"post": "This field is required."})

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise serializers.ValidationError({"post": "Invalid post ID."})

        serializer.save(author=self.request.user, post=post)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def feed_posts(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by("-created_at")
    serializer = PostSerializer(posts, many=True)
    return response.Response({"posts": serializer.data})


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        """Like a post if not already liked"""
        post = generics.get_object_or_404(Post, id=pk)
        like, created = Like.objects.get_or_create(author=request.user, post=post)

        if created:
            # Send notification to post author
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id,
            )
            return response.Response(
                {"message": "Post liked!"}, status=status.HTTP_201_CREATED
            )
        return response.Response(
            {"message": "You have already liked this post."},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Unlike a post if previously liked"""
        try:
            like = Like.objects.get(author=request.user, id=pk)
            like.delete()
            return response.Response(
                {"message": "Post unliked."}, status=status.HTTP_204_NO_CONTENT
            )
        except Like.DoesNotExist:
            return response.Response(
                {"message": "You haven't liked this post yet."},
                status=status.HTTP_400_BAD_REQUEST,
            )
