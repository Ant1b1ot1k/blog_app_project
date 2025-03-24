from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),  # refers the home function in views.py file
    path('about/', views.about, name='blog-about'),
]
