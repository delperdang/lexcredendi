from django.urls import path
from catechism import views

urlpatterns = [
    path('', views.home, name='catechism_home'),
    path('details/<code>/', views.details, name='catechism_details'),
    path('search', views.search, name='catechism_search'),
]
