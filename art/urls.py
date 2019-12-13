from django.urls import path
from art import views

urlpatterns = [
    path('', views.home, name='art_home'),
]
