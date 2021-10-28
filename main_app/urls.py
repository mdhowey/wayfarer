from django.urls import path, include
from main_app import views

urlpatterns = [
    path('', views.home, name="home"), # <- here we have added the new path
    path('profile/', views.profile, name="profile"), 
]