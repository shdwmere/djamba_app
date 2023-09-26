# produtos_files/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedidos
from .forms import PedidosForm

def home(request):
    return render(request, 'front_plataforma/home.html')

def ler_todos_pedidos(request):
    pedidos = {
        'pedidos': Pedidos.objects.all()
    }
    return render(request, 'front_plataforma/read_screen.html', pedidos)

def criar_pedido(request):
    form = PedidosForm()
    if request.method == 'POST':
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ler_todos_pedidos')
        print(form.errors)
    return render(request, 'front_plataforma/create_screen.html', {'form': form})

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
