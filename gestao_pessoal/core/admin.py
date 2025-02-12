from django.contrib import admin
from .models import Category, Transaction, CreditCard, Goal, Task, WishlistItem

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'user')
    list_filter = ('type', 'user')
    search_fields = ('name', 'description')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'amount', 'type', 'category', 'user')
    list_filter = ('type', 'payment_method', 'category', 'user')
    search_fields = ('description',)
    date_hierarchy = 'date'

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'limit', 'closing_day', 'due_day', 'user')
    list_filter = ('user',)
    search_fields = ('name',)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'target_amount', 'current_amount', 'deadline', 'type', 'user')
    list_filter = ('type', 'user')
    search_fields = ('name', 'description')
    date_hierarchy = 'deadline'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'due_date', 'user')
    list_filter = ('status', 'priority', 'user')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'estimated_price', 'priority', 'user')
    list_filter = ('priority', 'user')
    search_fields = ('name', 'description')
