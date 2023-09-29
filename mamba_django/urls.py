# projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from tracking_system import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracking_system/', include('tracking_system.urls')),
    path('admin/', admin.site.urls),
]
