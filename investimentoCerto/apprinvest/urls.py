from django.urls import path
from . import views

app_name = 'apprinvest'

urlpatterns = [
    # Páginas públicas
    path('', views.home, name='home'),
    path('noticias/', views.NewsList.as_view(), name='news_list'),
    path('noticias/<slug:slug>/', views.NewsDetail.as_view(), name='news_detail'),
    
    # Dashboard financeiro
    path('dashboard/', views.financial_dashboard, name='financial_dashboard'),
    path('api/indicator/<str:symbol>/', views.get_indicator_data, name='indicator_data'),
    
    # Área administrativa
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/logs/', views.api_logs, name='api_logs'),
]
