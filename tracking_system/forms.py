# app/forms.py
from django import forms
from .models import Pedidos

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = '__all__'
        widgets = {
            'id_pedido': forms.TextInput(),
            'codigo_rastreio': forms.TextInput(),
            'cpf_cliente': forms.TextInput(),
            'nome_cliente': forms.TextInput(),
            'email_cliente': forms.TextInput(),
            'data_registro': forms.DateInput(),
        }

class PesquisaForm(forms.Form):
    codigo_rastreio = forms.CharField(max_length=14, label="Track Code")