from django.db import models

class Pedidos(models.Model):
    id = models.AutoField(primary_key=True)
    id_pedido = models.CharField(max_length=12)
    codigo_rastreio = models.CharField(max_length=14)
    
    cpf_cliente = models.CharField(max_length=14)
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField(max_length=100)
    data_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_cliente
