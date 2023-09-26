# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('criar_pedido/', views.criar_pedido, name='criar_pedido'),
    path('ler_todos/', views.ler_todos_pedidos, name='ler_todos_pedidos'),
    path('atualizar_pedido/<int:pk>/', views.atualizar_pedido, name='atualizar_pedido'),
    path('deletar_pedido/<int:pk>/', views.deletar_pedido, name='deletar_pedido')
]