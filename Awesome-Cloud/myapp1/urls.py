from django.urls import path
from .views import page, sign, registration, delete

urlpatterns = [
    path('', page, name="home"),
    path("login/", sign, name="login"),
    path("registration/", registration, name="registration"),
    path("delete/<int:file_id>", delete, name="delete"),
]