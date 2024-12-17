# Bingo Online Multiplayer

Este é um jogo de Bingo multiplayer que permite que vários jogadores participem do mesmo jogo através da rede.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python listadas em `requirements.txt`

## Instalação

1. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

## Como Jogar

### Iniciando o Servidor

1. Em um computador que será o servidor, execute:
```bash
python server.py
```
O servidor iniciará na porta 8000.

### Conectando Jogadores

1. Em cada computador que deseja jogar, execute:
```bash
python bingo_client.py
```

2. Digite seu nome quando solicitado

3. O jogo conectará automaticamente ao servidor (por padrão, conecta em localhost:8000)

### Jogando

- Cada jogador receberá uma cartela com 16 números
- Qualquer jogador pode clicar em "Sortear Número" para sortear um novo número
- Os números sorteados são marcados automaticamente nas cartelas
- Quando um jogador completar sua cartela, pode clicar em "BINGO!"
- O servidor verificará se o jogador realmente ganhou

## Configuração para Jogar em Rede

Para jogar em computadores diferentes:

1. No arquivo `bingo_client.py`, altere a linha:
```python
self.sio.connect('http://localhost:8000')
```
para:
```python
self.sio.connect('http://IP_DO_SERVIDOR:8000')
```
Onde `IP_DO_SERVIDOR` é o endereço IP do computador que está rodando o servidor.

## Funcionalidades

- Interface gráfica intuitiva
- Suporte a múltiplos jogadores
- Verificação automática de números sorteados
- Sistema de log para acompanhar eventos do jogo
- Validação de vitória pelo servidor
- Notificações de entrada/saída de jogadores
