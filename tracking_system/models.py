from django.db import models

class Pedidos(models.Model):
    id = models.AutoField(primary_key=True)
    id_pedido = models.CharField(max_length=13)
    codigo_rastreio = models.CharField(max_length=16)
    
    cpf_cliente = models.CharField(max_length=14)
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField(max_length=100)
    data_registro = models.DateField(editable=True)

    def __str__(self):
        return self.nome_cliente
