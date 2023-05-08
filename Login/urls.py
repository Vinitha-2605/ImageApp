from django.urls import path
from . import views

urlpatterns =[
    path("Login", views.loginpage),
    path("register", views.signup),
    path("Logout", views.logout),
]
