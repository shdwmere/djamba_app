# produtos_files/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedidos
from .forms import PedidosForm, PesquisaForm

def home(request):
    return render(request, 'front_plataforma/home.html')

# Leitura
def ler_todos_pedidos(request):
    pedidos = {
        'pedidos': Pedidos.objects.all()
    }
    return render(request, 'front_plataforma/read_screen.html', pedidos)

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

    return render(request, 'front_plataforma/filter_screen.html', context)

def track_code(request):
    if request.method == 'POST':
        form = PesquisaForm(request.POST)
        if form.is_valid():
            codigo_rastreio = form.cleaned_data['codigo_rastreio']
            # Execute a consulta com base no código de rastreio
            pedidos = Pedidos.objects.filter(codigo_rastreio=codigo_rastreio)
            return render(request, 'front_plataforma/track_screen.html', {'pedidos': pedidos})
    else:
        form = PesquisaForm()
    
    return render(request, 'front_plataforma/home.html', {'form': form})

# Criação
def criar_pedido(request):
    form = PedidosForm()
    if request.method == 'POST':
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ler_todos_pedidos')
        print(form.errors)
    return render(request, 'front_plataforma/create_screen.html', {'form': form})


# Modificação
def atualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedidos, pk=pk)
    if request.method == 'POST':
        form = PedidosForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('ler_todos_pedidos')
    else:
        form = PedidosForm(instance=pedido)
    return render(request, 'front_plataforma/atualizar_screen.html', {'form': form})

def deletar_pedido(request, pk):
    pedido = get_object_or_404(Pedidos, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ler_todos_pedidos')
    return render(request, 'front_plataforma/deletar_screen.html', {'pedido': pedido})


