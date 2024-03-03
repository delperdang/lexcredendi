from django.urls import path
from meditation import views

urlpatterns = [
    path('', views.home, name='meditation_home'),
]
