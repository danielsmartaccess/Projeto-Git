from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import NewsArticle, FinancialIndicator, Category, APILog
from django.utils import timezone
import json

# Create your views here.

def home(request):
    """Página inicial com notícias em destaque e indicadores principais"""
    latest_news = NewsArticle.objects.filter(is_verified=True).order_by('-published_date')[:5]
    main_indicators = FinancialIndicator.objects.all()[:6]
    categories = Category.objects.all()

    context = {
        'latest_news': latest_news,
        'main_indicators': main_indicators,
        'categories': categories,
    }
    return render(request, 'apprinvest/home.html', context)

class NewsList(ListView):
    """Lista de notícias com paginação"""
    model = NewsArticle
    template_name = 'apprinvest/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = NewsArticle.objects.filter(is_verified=True)
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset.order_by('-published_date')

class NewsDetail(DetailView):
    """Detalhes de uma notícia específica"""
    model = NewsArticle
    template_name = 'apprinvest/news_detail.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_news'] = NewsArticle.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:3]
        return context

@login_required
def financial_dashboard(request):
    """Dashboard com indicadores financeiros e gráficos"""
    indicators = FinancialIndicator.objects.all()
    context = {
        'indicators': indicators,
        'last_update': timezone.now(),
    }
    return render(request, 'apprinvest/financial_dashboard.html', context)

def get_indicator_data(request, symbol):
    """API endpoint para obter dados históricos de um indicador"""
    indicator = get_object_or_404(FinancialIndicator, symbol=symbol)
    history = indicator.indicatorhistory_set.all().order_by('-timestamp')[:30]
    
    data = {
        'labels': [h.timestamp.strftime('%Y-%m-%d %H:%M') for h in history],
        'values': [float(h.value) for h in history],
    }
    return JsonResponse(data)

@staff_member_required
def admin_dashboard(request):
    """Painel administrativo para gerenciamento de conteúdo"""
    recent_news = NewsArticle.objects.order_by('-created_at')[:10]
    recent_logs = APILog.objects.order_by('-timestamp')[:20]
    
    context = {
        'recent_news': recent_news,
        'recent_logs': recent_logs,
        'indicator_count': FinancialIndicator.objects.count(),
        'news_count': NewsArticle.objects.count(),
    }
    return render(request, 'apprinvest/admin_dashboard.html', context)

@staff_member_required
def api_logs(request):
    """Visualização dos logs de integração"""
    logs = APILog.objects.all().order_by('-timestamp')
    paginator = Paginator(logs, 50)
    page = request.GET.get('page')
    logs_page = paginator.get_page(page)
    
    context = {
        'logs': logs_page,
    }
    return render(request, 'apprinvest/api_logs.html', context)
