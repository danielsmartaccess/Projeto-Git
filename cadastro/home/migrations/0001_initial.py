# Generated by Django 5.1.5 on 2025-01-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('tipo_socio', models.CharField(choices=[('titular', 'Titular'), ('dependente', 'Dependente'), ('convidado', 'Convidado')], max_length=20)),
                ('endereco', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
