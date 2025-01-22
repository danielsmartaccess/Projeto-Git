from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    """Categoria para classificação das notícias"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    """Modelo para armazenar notícias financeiras"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    source_url = models.URLField()
    source_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class FinancialIndicator(models.Model):
    """Modelo para armazenar indicadores e cotações financeiras"""
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)
    current_value = models.DecimalField(max_digits=15, decimal_places=4)
    variation = models.DecimalField(max_digits=7, decimal_places=2)
    last_update = models.DateTimeField()
    source = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class IndicatorHistory(models.Model):
    """Histórico de valores dos indicadores financeiros"""
    indicator = models.ForeignKey(FinancialIndicator, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']

class APILog(models.Model):
    """Logs de integração com APIs externas"""
    LEVEL_CHOICES = [
        ('INFO', 'Information'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error'),
    ]
    
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    source = models.CharField(max_length=100)  # Nome da API ou serviço
    message = models.TextField()
    details = models.JSONField(null=True, blank=True)  # Armazena detalhes adicionais em formato JSON
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.timestamp} - {self.level}: {self.source}"

class UserProfile(models.Model):
    """Perfil estendido para usuários"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_categories = models.ManyToManyField(Category, blank=True)
    notification_preferences = models.JSONField(default=dict)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
