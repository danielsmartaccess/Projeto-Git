# Sistema de Gestão Financeira e Pessoal

Sistema web desenvolvido com Django e Django Rest Framework para gerenciamento financeiro e planejamento pessoal.

## Funcionalidades

- Autenticação de usuários com JWT
- Gestão de finanças pessoais
- Planejamento pessoal e profissional
- Dashboard dinâmico com gráficos
- API RESTful

## Requisitos

- Python 3.8+
- Django 5.0.1
- Django Rest Framework 3.14.0
- Outras dependências listadas em requirements.txt

## Instalação

1. Clone o repositório
```bash
git clone [url-do-repositorio]
```

2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crie um superusuário
```bash
python manage.py createsuperuser
```

6. Inicie o servidor
```bash
python manage.py runserver
```

## Estrutura do Projeto

```
gestao_pessoal/
├── core/                    # Aplicação principal
│   ├── models/             # Modelos do banco de dados
│   ├── serializers/        # Serializers da API
│   ├── views/              # Views da API
│   └── urls.py             # URLs da aplicação
├── authentication/         # App de autenticação
├── config/                # Configurações do projeto
└── manage.py
```

## API Endpoints

- `/api/auth/` - Endpoints de autenticação
- `/api/finances/` - Gestão financeira
- `/api/planning/` - Planejamento pessoal
- `/api/dashboard/` - Dados do dashboard

## Licença

MIT
