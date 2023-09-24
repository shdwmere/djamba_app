# produtos_files/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'front_plataforma/home.html')