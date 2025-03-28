from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.email} - {self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Coment by {self.author.email} on {self.post.title}"


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, default=1, related_name="likes"
    )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("author", "post")  # Ensures a user can like a post only once

    def __str__(self):
        return f"{self.author.email} liked {self.post.title}"
