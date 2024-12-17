from flask import Flask, jsonify, request
import socketio
import random
import eventlet

# Configuração do Flask e SocketIO
app = Flask(__name__)
sio = socketio.Server(cors_allowed_origins='*')

class BingoServer:
    def __init__(self):
        self.drawn_numbers = []
        self.players = {}  # {sid: player_name}
        self.cards = {}    # {sid: card_numbers}
        self.game_active = False
        self.current_turn = None
    
    def generate_card(self):
        """Gera uma cartela com 16 números únicos entre 0 e 99"""
        return random.sample(range(100), 16)
    
    def draw_number(self):
        """Sorteia um novo número que ainda não foi sorteado"""
        available = set(range(100)) - set(self.drawn_numbers)
        if available:
            number = random.choice(list(available))
            self.drawn_numbers.append(number)
            return number
        return None
    
    def check_winner(self, sid):
        """Verifica se o jogador ganhou"""
        if sid not in self.cards:
            return False
        player_card = set(self.cards[sid])
        drawn_numbers = set(self.drawn_numbers)
        return player_card.issubset(drawn_numbers)

# Instância do servidor de bingo
bingo_server = BingoServer()

@sio.on('connect')
def connect(sid, environ):
    """Chamado quando um cliente se conecta"""
    print(f'Cliente conectado: {sid}')

@sio.on('disconnect')
def disconnect(sid):
    """Chamado quando um cliente desconecta"""
    if sid in bingo_server.players:
        player_name = bingo_server.players[sid]
        print(f'Cliente desconectado: {player_name} ({sid})')
        del bingo_server.players[sid]
        del bingo_server.cards[sid]
        sio.emit('player_left', {'player_name': player_name})

@sio.on('join_game')
def join_game(sid, player_name):
    """Chamado quando um jogador entra no jogo"""
    card = bingo_server.generate_card()
    bingo_server.players[sid] = player_name
    bingo_server.cards[sid] = card
    
    # Envia a cartela para o jogador
    sio.emit('card_assigned', {
        'card': card,
        'player_name': player_name,
        'current_numbers': bingo_server.drawn_numbers
    }, room=sid)
    
    # Notifica todos sobre o novo jogador
    sio.emit('player_joined', {
        'player_name': player_name,
        'total_players': len(bingo_server.players)
    }, broadcast=True)

@sio.on('draw_number')
def draw_number(sid):
    """Chamado quando é solicitado um novo número"""
    if sid in bingo_server.players:
        number = bingo_server.draw_number()
        if number is not None:
            sio.emit('number_drawn', {
                'number': number,
                'drawn_by': bingo_server.players[sid]
            }, broadcast=True)
        else:
            sio.emit('game_over', room=sid)

@sio.on('check_bingo')
def check_bingo(sid):
    """Chamado quando um jogador clama bingo"""
    if bingo_server.check_winner(sid):
        winner_name = bingo_server.players[sid]
        sio.emit('winner_found', {
            'winner_name': winner_name,
            'card': bingo_server.cards[sid]
        }, broadcast=True)
        return True
    return False

if __name__ == '__main__':
    # Wrap Flask application with socketio's middleware
    app = socketio.WSGIApp(sio, app)
    
    # Inicia o servidor
    print("Servidor Bingo iniciado na porta 8000...")
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
