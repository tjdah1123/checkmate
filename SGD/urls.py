from re import template
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index),
    path("login/", views.login),   #auth_views.LoginView.as_view(template_name="login.html")
    path("log/", views.log),
    path('logout/', views.logout), #auth_views.LogoutView.as_view()
    path("attendance/", views.attendance),
    path("cam_1/", views.cam_1),
    path("cam_2/", views.cam_2),
    path("check/", views.check),
    path("right/", views.right),
    
    
    
]
