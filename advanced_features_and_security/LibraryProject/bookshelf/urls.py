from django.urls import path
from . import views
urlpatterns = [path("form/", views.form_example, name="form-view")]
