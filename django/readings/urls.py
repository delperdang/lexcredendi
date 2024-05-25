from django.urls import path
from readings import views

urlpatterns = [
    path('', views.home, name='readings_home'),
]
