from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'meu_app/home.html')

def about(request):
    return render(request, 'meu_app/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Criar novo objeto Contact
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # Adicionar mensagem de sucesso
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('contact')
        
    return render(request, 'meu_app/contact.html')