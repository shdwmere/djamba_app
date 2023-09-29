# produtos_files/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Pedidos
from .forms import PedidosForm, PesquisaForm

# api
from django.http import BadHeaderError, HttpResponse
from .serializers import PedidosSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


def home(request):
    return render(request, 'core/home.html')

# Listar todos / Filtrar pedidos
def ler_todos_pedidos(request):
    pedidos = {
        'pedidos': Pedidos.objects.all()
    }
    return render(request, 'utils/read_screen.html', pedidos)

def filtrar_pedidos(request, data_filtrada = None):
    data_filtrada = request.GET.get('data_filtrada')
    if data_filtrada:
        pedidos = Pedidos.objects.filter(data_registro = data_filtrada)
    else:
        pedidos = Pedidos.objects.all()

    contagem = pedidos.count()
    
    context = {
        'pedidos': pedidos,
        'contagem': contagem
    }

    return render(request, 'core/filter_screen.html', context)


# Rastreio
def track_code(request):
    if request.method == 'POST':
        form = PesquisaForm(request.POST)
        if form.is_valid():
            codigo_rastreio = form.cleaned_data['codigo_rastreio']
            # Execute a consulta com base no código de rastreio
            pedidos = Pedidos.objects.filter(codigo_rastreio=codigo_rastreio)
            return render(request, 'core/track_screen.html', {'pedidos': pedidos})
    else:
        form = PesquisaForm()
    
    return render(request, 'frontend/home.html', {'form': form})


# Modificação (Update, Delete)
def atualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedidos, pk=pk)
    if request.method == 'POST':
        form = PedidosForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('ler_todos_pedidos')
    else:
        form = PedidosForm(instance=pedido)
    return render(request, 'utils/atualizar_screen.html', {'form': form})

def deletar_pedido(request, pk):
    pedido = get_object_or_404(Pedidos, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ler_todos_pedidos')
    return render(request, 'utils/deletar_screen.html', {'pedido': pedido})


# Ações (mailing)
def enviar_email(request):
    subject = 'tracking service'
    message = 'testando mailing da aplicação.'
    from_email = 'suporte@www.mambalog.tech'
    recipient_list = ['caio.souza@topshipping.com.br']

    context = {
        'subject': subject,
        'message': message,
        'from_email': from_email,
        'recipient_list': recipient_list
    }

    if request.method == 'POST':
        try:
            send_mail(subject, message, from_email, recipient_list)
            # página de sucesso
            return render(request, 'mail/email_enviado.html', context)
        except BadHeaderError:
            # Lida com cabeçalhos de e-mail malformados
            return HttpResponse('Erro no envio do e-mail. Por favor, revise os detalhes.')
        except Exception as e:
            # Lida com outros erros de envio de e-mail
            return HttpResponse(f'Erro no envio do e-mail: {str(e)}')
    
    return render(request, 'mail/email_screen.html', context)
    

# API ViewSet
class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer

    def create_item(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)