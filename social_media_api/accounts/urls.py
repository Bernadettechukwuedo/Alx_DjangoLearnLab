from django.urls import path, include
from .views import register_user, login_user, profile

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("profile/", profile, name="profile"),
]
