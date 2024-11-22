from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("details/<int:user_id>", views.user_details, name="user-details"),
]
