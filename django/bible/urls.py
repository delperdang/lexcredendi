from django.urls import path
from bible import views

urlpatterns = [
    path('', views.home, name='bible_home'),
    path('details/<code>/', views.details, name='bible_details'),
    path('search', views.search, name='bible_search'),
]
