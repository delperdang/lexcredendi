from django.urls import path
from doctrine import views


urlpatterns = [
    path('', views.home, name='doctrine_home'),
    path('details/<code>/', views.details, name='doctrine_details'),
    path('search', views.search, name='doctrine_search'),
]
