from django.contrib import admin
from .models import Category, NewsArticle, FinancialIndicator, IndicatorHistory, APILog, UserProfile

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'source_name', 'published_date', 'is_verified')
    list_filter = ('category', 'source_name', 'is_verified', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'

@admin.register(FinancialIndicator)
class FinancialIndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'current_value', 'variation', 'last_update')
    list_filter = ('source',)
    search_fields = ('name', 'symbol')

@admin.register(IndicatorHistory)
class IndicatorHistoryAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'value', 'timestamp')
    list_filter = ('indicator', 'timestamp')
    date_hierarchy = 'timestamp'

@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'level', 'source', 'message')
    list_filter = ('level', 'source', 'timestamp')
    search_fields = ('message', 'details')
    date_hierarchy = 'timestamp'

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_login_ip')
    list_filter = ('favorite_categories',)
    search_fields = ('user__username', 'user__email')
