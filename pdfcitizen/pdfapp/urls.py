from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('reg', views.reg),
    path('login', views.login),
    path('search', views.search),
]
