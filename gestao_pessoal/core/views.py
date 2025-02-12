from django.shortcuts import render
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Category, Transaction, CreditCard, Goal, Task, WishlistItem, Bill
from .serializers import (CategorySerializer, TransactionSerializer, CreditCardSerializer,
                        GoalSerializer, TaskSerializer, WishlistItemSerializer, BillSerializer)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Sum
from datetime import datetime
from django.utils import timezone

# Create your views here.

class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class CategoryViewSet(BaseModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['type']
    search_fields = ['name', 'description']
    ordering_fields = ['name']

class TransactionViewSet(BaseModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = ['type', 'payment_method', 'category']
    search_fields = ['description']
    ordering_fields = ['date', 'amount']

class CreditCardViewSet(BaseModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    search_fields = ['name']
    ordering_fields = ['name', 'due_day']

class GoalViewSet(BaseModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    filterset_fields = ['type']
    search_fields = ['name', 'description']
    ordering_fields = ['deadline', 'target_amount']

class TaskViewSet(BaseModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at', 'priority']

class WishlistItemViewSet(BaseModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    filterset_fields = ['priority']
    search_fields = ['name', 'description']
    ordering_fields = ['estimated_price', 'priority']

class BillViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gerenciar contas a pagar
    """
    serializer_class = BillSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['paid', 'category']
    search_fields = ['description']
    ordering_fields = ['due_date', 'amount']
    ordering = ['due_date']

    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now()
        current_month = today.month
        current_year = today.year

        # Cálculos financeiros do mês atual
        transactions = Transaction.objects.filter(
            user=self.request.user,
            date__month=current_month,
            date__year=current_year
        )

        income = transactions.filter(type='income').aggregate(
            total=Sum('amount'))['total'] or 0
        expenses = transactions.filter(type='expense').aggregate(
            total=Sum('amount'))['total'] or 0

        context.update({
            'total_income': income,
            'total_expenses': expenses,
            'balance': income - expenses,
            'recent_transactions': transactions.order_by('-date')[:5],
            'upcoming_bills': Bill.objects.filter(
                user=self.request.user,
                due_date__gte=today
            ).order_by('due_date')[:5],
            'goals': Goal.objects.filter(user=self.request.user)
        })

        return context

class TransactionListView(LoginRequiredMixin, TemplateView):
    template_name = 'core/transactions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(user=self.request.user).order_by('-date')
        return context

class CategoryListView(LoginRequiredMixin, TemplateView):
    template_name = 'core/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(user=self.request.user)
        return context

class CreditCardListView(LoginRequiredMixin, TemplateView):
    template_name = 'core/credit_cards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['credit_cards'] = CreditCard.objects.filter(user=self.request.user)
        return context

class GoalListView(LoginRequiredMixin, TemplateView):
    template_name = 'core/goals.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = Goal.objects.filter(user=self.request.user)
        return context

class TaskListView(LoginRequiredMixin, TemplateView):
    template_name = 'core/tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        return context

class WishlistView(LoginRequiredMixin, TemplateView):
    template_name = 'core/wishlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wishlist_items'] = WishlistItem.objects.filter(user=self.request.user)
        return context

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
