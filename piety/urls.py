from django.urls import path
from piety import views


urlpatterns = [
    path('', views.home, name='piety_home'),
    path('details/<code>/', views.details, name='piety_details'),
    path('search', views.search, name='piety_search'),
]
