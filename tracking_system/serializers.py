from rest_framework import serializers
from .models import Pedidos

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = ('id', 'id_pedido', 'codigo_rastreio', 'cpf_cliente', 'nome_cliente', 'email_cliente', 'data_registro')
