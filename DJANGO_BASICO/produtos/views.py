from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def ver_produto(request):
    nome = 'Daniel Steinbruch Pere'
    return  render(request, 'ver_produto.html',{'nome': nome })

def inserir_produto(request):
    return  render(request, 'inserir_produto.html')