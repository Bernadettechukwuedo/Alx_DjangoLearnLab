from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


"""
Authentication & Permissions Configuration:

This API uses Django REST Framework's (DRF) Token Authentication to secure endpoints.
- Users must authenticate using a token, which can be obtained by sending their credentials 
  (username and password) to the `/api/token/` endpoint.
- By default, all API endpoints require authentication unless explicitly stated otherwise.

Key Components:
1. **Token Authentication**: Configured in `settings.py` under `DEFAULT_AUTHENTICATION_CLASSES`.
2. **Permissions**: Controlled using `DEFAULT_PERMISSION_CLASSES`, enforcing `IsAuthenticated` 
   for all views unless overridden at the view level.
3. **Token Retrieval**: Users can obtain an authentication token via `rest_framework.authtoken.views.obtain_auth_token`.
4. **Protected API Views**: Only authenticated users with a valid token can access views that have 
   `permission_classes = [IsAuthenticated]`.

To use a token for authentication, include it in the request headers:
    Authorization: Token <your_token>

Ensure to handle authentication errors properly, such as missing or invalid tokens.
"""


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
