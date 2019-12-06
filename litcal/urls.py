from django.urls import path
from litcal import views

urlpatterns = [
    path('', views.home, name='litcal_home'),
]
