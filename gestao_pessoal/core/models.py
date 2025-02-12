from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    """Model for expense and income categories"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f"{self.name} ({self.type})"

class Transaction(models.Model):
    """Model for financial transactions"""
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('transfer', 'Bank Transfer'),
        ('pix', 'PIX'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    installments = models.PositiveIntegerField(default=1)
    current_installment = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.date} - {self.description} ({self.amount})"

class CreditCard(models.Model):
    """Model for credit card management"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    closing_day = models.PositiveIntegerField()  # Day of month
    due_day = models.PositiveIntegerField()  # Day of month
    
    def __str__(self):
        return self.name

class Goal(models.Model):
    """Model for financial goals"""
    GOAL_TYPES = [
        ('savings', 'Savings'),
        ('investment', 'Investment'),
        ('debt_payment', 'Debt Payment'),
        ('purchase', 'Purchase'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()
    type = models.CharField(max_length=20, choices=GOAL_TYPES)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    """Model for personal tasks and planning"""
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class WishlistItem(models.Model):
    """Model for wishlist items"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)
    priority = models.CharField(max_length=10, choices=Task.PRIORITY_CHOICES, default='medium')
    url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Bill(models.Model):
    """Modelo para contas a pagar"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f"{self.description} - R${self.amount} (Vence: {self.due_date})"
