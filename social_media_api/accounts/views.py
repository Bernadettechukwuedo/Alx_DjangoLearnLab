from django.shortcuts import render
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    FollowSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from .models import CustomUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions


# Create your views here.


@permission_classes([AllowAny])
@api_view(["POST"])
def register_user(request):

    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
@api_view(["POST"])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user": {
                    "id": user.id,
                    "email": user.email,
                },
            },
            status=status.HTTP_200_OK,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def profile(request):
    if not request.user.is_authenticated:
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    serializer = UserProfileSerializer(request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)


class FollowViewSet(viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer

    @action(detail=False, methods=["post"])
    def follow(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(CustomUser, id=serializer.validated_data["user_id"])

        if request.user.follow(user):
            return Response({"status": "following"}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Already following or invalid user"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=False, methods=["post"])
    def unfollow(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = CustomUser.objects.get(id=serializer.validated_data["user_id"])

        if request.user.unfollow(user):
            return Response({"status": "unfollowed"}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Not following or invalid user"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=False, methods=["get"])
    def profile(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    success = request.user.follow(target_user)  # Uses the model's follow() method
    if success:
        return Response(
            {"status": "success", "message": f"Followed {target_user.email}"}
        )
    return Response(
        {"status": "failed", "message": "Already following or invalid action"},
        status=400,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    success = request.user.unfollow(target_user)  # Uses the model's unfollow() method
    if success:
        return Response(
            {"status": "success", "message": f"Unfollowed {target_user.email}"}
        )
    return Response(
        {"status": "failed", "message": "Not following or invalid action"}, status=400
    )


class Follow(generics.GenericAPIView):
    pass
