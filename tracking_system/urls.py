# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('ler_todos/', views.ler_todos_pedidos, name='ler_todos_pedidos'),
    path('atualizar_pedido/<int:pk>/', views.atualizar_pedido, name='atualizar_pedido'),
    path('deletar_pedido/<int:pk>/', views.deletar_pedido, name='deletar_pedido'),
    path('filtrar/', views.filtrar_pedidos, name='filtrar_pedidos'),
    path('track/', views.track_code, name='track_code'),
    path('email/', views.enviar_email, name='enviar_email')
]