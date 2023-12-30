"""lexcredendi URL Configuration

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tz_detect/', include('tz_detect.urls')),
    path('', include('home.urls')),
    path('apologetics/', include('apologetics.urls')),
    path('art/', include('art.urls')),
    path('bible/', include('bible.urls')),
    path('catechism/', include('catechism.urls')),
    path('doctrine/', include('doctrine.urls')),
    path('litcal/', include('litcal.urls')),
    path('meditation/', include('meditation.urls')),
    path('piety/', include('piety.urls')),
    path('prayer/', include('prayer.urls')),
    path('readings/', include('readings.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
