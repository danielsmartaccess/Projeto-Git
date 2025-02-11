from django import path
from .views import listar_usuarios, listar_planos, listar_assinaturas

urlpatterns = [
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('planos/', listar_planos, name='listar_planos'),
    path('assinaturas/', listar_assinaturas, name='listar_assinaturas'),
]