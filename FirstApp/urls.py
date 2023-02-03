from django.contrib import admin
from django.urls import path
from django.urls import include
from FirstApp import views

urlpatterns = [
    path("", views.index, name='home'), #here you're adding visual pages and their names.
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
]