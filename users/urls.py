from django.urls import path
from . import views


urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("login", views.LogIn.as_view()),
    path("logout", views.Logout.as_view()),
    path("jwt-login", views.JWTLogIn.as_view()),
    path("change-password", views.ChangePassword.as_view()),
]
