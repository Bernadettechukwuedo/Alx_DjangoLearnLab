from django.urls import path, include
from .views import (
    register_user,
    login_user,
    profile,
    FollowViewSet,
    follow_user,
    unfollow_user,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("profile/", profile, name="profile"),
    path("follow/<int:user_id>/", follow_user, name="follow"),
    path("unfollow/<int:user_id>/", unfollow_user, name="unfollow"),
]
