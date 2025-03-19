from django.urls import path, include
from .views import register, login_user, profile, logout_user

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", logout_user, name="logout"),
]
