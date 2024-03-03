from django.urls import path
from art import views

urlpatterns = [
    path('', views.home, name='art_home'),
    path('details/<album>/', views.details, name='art_details'),
]
