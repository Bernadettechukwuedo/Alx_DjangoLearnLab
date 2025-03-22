from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, Comment

from taggit.forms import TagField, TagWidget


class SignUpForm(UserCreationForm):
    email = forms.EmailField()


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {"tags": TagWidget()}

    def save(self, commit=True, user=None):
        post = super().save(commit=False)

        if user:  # Ensure user is set
            post.author = user
        if commit:
            post.save()
            self.save_m2m()

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
