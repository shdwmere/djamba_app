# projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from tracking_system import views
from tracking_system.views import PedidosViewSet
from rest_framework import routers

# routing rest api
router = routers.DefaultRouter()
router.register(r'pedidos', PedidosViewSet) # acesse /pedidos para consumir a rest api

urlpatterns = [
    path('', views.home, name='home'),
    path('tracking_system/', include('tracking_system.urls')),
    path('admin/', admin.site.urls),
    # api
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/create/', PedidosViewSet.as_view({'post': 'create_item'}), name='create_item'),
]
