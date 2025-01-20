from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        # Captura os dados do formulário
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        tipo_socio = request.POST.get('tipo_socio')
        endereco = request.POST.get('endereco')

        # Aqui você pode adicionar a lógica para salvar os dados no banco de dados
        # Por enquanto, apenas mostraremos uma mensagem de sucesso
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('home')

    return render(request, 'home.html')