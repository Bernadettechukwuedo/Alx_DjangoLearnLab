from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, Comment


class SignUpForm(UserCreationForm):
    email = forms.EmailField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

        def save(self, commit=True, user=None):
            post = super().save(commit=False)

            if post:
                post.author = user
            if commit:
                post.save()

            return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

        def save(self, commit=True, user=None, post=None):
            comment = super().save(commit=False)

            if comment:
                comment.author = user
                comment.post = post
            if commit:
                comment.save()

            return comment