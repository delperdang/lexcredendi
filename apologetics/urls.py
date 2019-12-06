from django.urls import path
from apologetics import views

urlpatterns = [
    path('', views.home, name='apologetics_home'),
    path('details/<code>/', views.details, name='apologetics_details'),
]
