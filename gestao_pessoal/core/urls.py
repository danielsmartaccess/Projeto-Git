from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, TransactionViewSet, CreditCardViewSet,
    GoalViewSet, TaskViewSet, WishlistItemViewSet, BillViewSet,
    DashboardView, TransactionListView, CategoryListView,
    CreditCardListView, GoalListView, TaskListView, WishlistView,
    ProfileView
)

# Router para API endpoints
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'credit-cards', CreditCardViewSet, basename='creditcard')
router.register(r'goals', GoalViewSet, basename='goal')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'wishlist', WishlistItemViewSet, basename='wishlist')
router.register(r'bills', BillViewSet, basename='bill')

# URLs para views de template
urlpatterns = [
    # Template views
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('transactions/', TransactionListView.as_view(), name='transactions'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('credit-cards/', CreditCardListView.as_view(), name='credit-cards'),
    path('goals/', GoalListView.as_view(), name='goals'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # API endpoints
    path('api/', include(router.urls)),
]
