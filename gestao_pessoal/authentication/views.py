from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .forms import CustomUserCreationForm
from .serializers import UserSerializer, UserUpdateSerializer

User = get_user_model()

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class UserDetailView(generics.RetrieveUpdateAPIView):
    """View for retrieving and updating user details"""
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
