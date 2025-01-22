# Investimento Certo - Portal de Notícias e Indicadores Financeiros

Portal web que fornece notícias financeiras atualizadas e indicadores do mercado em tempo real.

## Características

- Notícias financeiras de fontes confiáveis (Valor Econômico, InfoMoney, Reuters)
- Indicadores financeiros em tempo real via Yahoo Finance
- Dashboard interativo com gráficos
- Sistema de autenticação de usuários
- Painel administrativo para gerenciamento de conteúdo
- Atualização automática de dados

## Requisitos

- Python 3.8+
- SQLite (incluído no Python)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/investimentoCerto.git
cd investimentoCerto
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

## Executando o Projeto

1. Inicie o servidor Django:
```bash
python manage.py runserver
```

2. Acesse o site em `http://localhost:8000`

O sistema iniciará automaticamente as tarefas agendadas para:
- Atualizar indicadores financeiros a cada 5 minutos
- Buscar novas notícias a cada 15 minutos

## Estrutura do Projeto

- `apprinvest/`: Aplicação principal
  - `models.py`: Definição dos modelos de dados
  - `views.py`: Views e lógica de negócios
  - `scheduler.py`: Tarefas agendadas
  - `templates/`: Templates HTML
  - `static/`: Arquivos estáticos (CSS, JS, imagens)

## APIs Utilizadas

- Yahoo Finance: Para cotações e indicadores financeiros
- RSS Feeds: Valor Econômico, InfoMoney, Reuters

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
