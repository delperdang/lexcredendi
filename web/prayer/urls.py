from django.urls import path
from prayer import views


urlpatterns = [
    path('', views.home, name='prayer_home'),
    path('details/<code>/', views.details, name='prayer_details'),
    path('search', views.search, name='prayer_search'),
]
