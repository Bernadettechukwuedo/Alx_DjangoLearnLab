from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.list_books, name="list_books"),
    path(
        "library/<int:pk>/", views.list_availabilityView.as_view(), name="list_details"
    ),
]
