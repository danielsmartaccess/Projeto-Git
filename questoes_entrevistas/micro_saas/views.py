from django.shortcuts import render
from .models import Usuario, Plano, Assinatura

# View para listar usuários

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

# View para listar planos

def listar_planos(request):
    planos = Plano.objects.all()
    return render(request, 'planos.html', {'planos': planos})

# View para listar assinaturas

def listar_assinaturas(request):
    assinaturas = Assinatura.objects.filter(status=True)
    return render(request, 'assinaturas.html', {'assinaturas': assinaturas})