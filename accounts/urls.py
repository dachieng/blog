from re import template
from unicodedata import name
from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("register/",views.register,name="register"),
    path("profile/",views.profile,name="profile"),
    path("login/",auth_views.LoginView.as_view(template_name="accounts/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="accounts/logout.html"),name='logout')
]