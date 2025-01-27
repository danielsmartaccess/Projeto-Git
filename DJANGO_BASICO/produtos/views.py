from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Pessoa

# Create your views here.
def ver_produto(request):
    if request.method == 'GET':
        nome = 'Daniel Steinbruch Pere'
        return  render(request, 'ver_produto.html',{'nome': nome })
    elif request.method == 'POST':
        return HttpResponse(f'Nome: {request.POST.get("nome")} <br> Idade: {request.POST.get("idade")}')

#def inserir_produto(request):
    return  render(request, 'inserir_produto.html')