from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Socio
from django.conf import settings

def index(request):
    # Se o usuário já estiver autenticado, redireciona para o cadastro
    if request.user.is_authenticated:
        return redirect('cadastro')
    return render(request, 'index.html')

def login_view(request):
    # Se o usuário já estiver autenticado, redireciona para o cadastro
    if request.user.is_authenticated:
        return redirect('cadastro')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember', False)
        
        if not username or not password:
            messages.error(request, 'Por favor, preencha todos os campos')
            return render(request, 'login.html')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            if not remember_me:
                request.session.set_expiry(0)  # Sessão expira ao fechar o navegador
            else:
                # Sessão dura 2 semanas
                request.session.set_expiry(1209600)
            
            messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('cadastro')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
            
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema com sucesso!')
    return redirect('index')

# Redireciona para cadastro
@login_required(login_url='login')
def home(request):
    return redirect('cadastro')

@login_required(login_url='login')
def cadastro(request):
    if request.method == 'POST':
        try:
            # Captura e valida os dados
            nome = request.POST.get('nome')
            cpf = request.POST.get('cpf')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            data_nascimento = request.POST.get('data_nascimento')
            tipo_socio = request.POST.get('tipo_socio')
            endereco = request.POST.get('endereco')

            # Validações básicas
            if not all([nome, cpf, email, telefone, data_nascimento, tipo_socio, endereco]):
                messages.error(request, 'Todos os campos são obrigatórios.')
                return render(request, 'cadastro.html')

            # Remove caracteres especiais do CPF e telefone
            cpf = ''.join(filter(str.isdigit, cpf))
            telefone = ''.join(filter(str.isdigit, telefone))

            # Cria o novo sócio
            socio = Socio.objects.create(
                nome=nome,
                cpf=cpf,
                email=email,
                telefone=telefone,
                data_nascimento=data_nascimento,
                tipo_socio=tipo_socio,
                endereco=endereco
            )
            
            print(f"Sócio cadastrado com sucesso: {socio.nome} (ID: {socio.id})")
            messages.success(request, 'Sócio cadastrado com sucesso!')
            return redirect('cadastro')
            
        except Exception as e:
            print(f"Erro ao cadastrar sócio: {str(e)}")
            messages.error(request, f'Erro ao cadastrar sócio: {str(e)}')
    
    return render(request, 'cadastro.html')

@login_required(login_url='login')
def consulta(request):
    search_query = request.GET.get('search', '')
    tipo_filter = request.GET.get('tipo', '')
    
    socios = Socio.objects.all()
    
    if search_query:
        socios = socios.filter(
            Q(nome__icontains=search_query) |
            Q(cpf__icontains=search_query)
        )
    
    if tipo_filter:
        socios = socios.filter(tipo_socio=tipo_filter)
    
    paginator = Paginator(socios, 10)  # 10 items per page
    page = request.GET.get('page')
    socios = paginator.get_page(page)
    
    return render(request, 'consulta.html', {'socios': socios})

@login_required(login_url='login')
def delete_socio(request, socio_id):
    if request.method == 'POST':
        socio = get_object_or_404(Socio, id=socio_id)
        nome_socio = socio.nome
        socio.delete()
        messages.success(request, f'Sócio {nome_socio} excluído com sucesso!')
    return redirect('consulta')