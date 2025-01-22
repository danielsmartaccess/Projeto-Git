from django.db import models

# Create your models here.

class Socio(models.Model):
    TIPO_SOCIO_CHOICES = [
        ('titular', 'Titular'),
        ('dependente', 'Dependente'),
        ('convidado', 'Convidado'),
    ]
    
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    tipo_socio = models.CharField(max_length=20, choices=TIPO_SOCIO_CHOICES)
    endereco = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"

    class Meta:
        ordering = ['nome']
