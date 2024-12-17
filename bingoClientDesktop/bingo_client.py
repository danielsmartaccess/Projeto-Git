import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import socketio
import json

class BingoCard:
    def __init__(self, master, player_name, card_numbers):
        """Inicializa uma cartela de bingo"""
        self.frame = tk.LabelFrame(master, text=f"Cartela - {player_name}", padx=10, pady=5)
        self.numbers = sorted(card_numbers)
        self.marked = set()
        self.buttons = []
        self._create_card()
    
    def _create_card(self):
        """Cria a interface gráfica da cartela"""
        for i, number in enumerate(self.numbers):
            row = i // 4
            col = i % 4
            btn = tk.Button(
                self.frame,
                text=str(number),
                width=5,
                height=2,
                command=lambda n=number: self._mark_number(n)
            )
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append((number, btn))
    
    def _mark_number(self, number):
        """Marca um número na cartela"""
        if number in self.marked:
            self.marked.remove(number)
            self._update_button_color(number, 'SystemButtonFace')
        else:
            self.marked.add(number)
            self._update_button_color(number, 'light green')
    
    def _update_button_color(self, number, color):
        """Atualiza a cor do botão"""
        for num, btn in self.buttons:
            if num == number:
                btn.configure(bg=color)
                break
    
    def mark_drawn_number(self, number):
        """Marca um número sorteado automaticamente"""
        if number in self.numbers and number not in self.marked:
            self.marked.add(number)
            self._update_button_color(number, 'light green')

class BingoGame:
    def __init__(self):
        """Inicializa o jogo de Bingo"""
        self.root = tk.Tk()
        self.root.title("Jogo de Bingo Online")
        self.setup_gui()
        self.setup_socket()
    
    def setup_socket(self):
        """Configura a conexão Socket.IO"""
        self.sio = socketio.Client()
        
        @self.sio.on('connect')
        def on_connect():
            print('Conectado ao servidor!')
        
        @self.sio.on('disconnect')
        def on_disconnect():
            print('Desconectado do servidor!')
        
        @self.sio.on('card_assigned')
        def on_card_assigned(data):
            self.create_card(data['card'])
            # Marca números já sorteados
            for number in data['current_numbers']:
                self.handle_drawn_number(number)
        
        @self.sio.on('number_drawn')
        def on_number_drawn(data):
            self.handle_drawn_number(data['number'])
            self.log_message(f"Número sorteado: {data['number']} (por {data['drawn_by']})")
        
        @self.sio.on('winner_found')
        def on_winner_found(data):
            messagebox.showinfo("Vencedor!", f"Jogador {data['winner_name']} ganhou!")
            self.log_message(f"BINGO! Jogador {data['winner_name']} venceu!")
        
        @self.sio.on('player_joined')
        def on_player_joined(data):
            self.log_message(f"Jogador {data['player_name']} entrou (Total: {data['total_players']})")
        
        @self.sio.on('player_left')
        def on_player_left(data):
            self.log_message(f"Jogador {data['player_name']} saiu")
    
    def setup_gui(self):
        """Configura a interface gráfica"""
        # Frame principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)
        
        # Área de cartelas
        self.cards_frame = tk.Frame(self.main_frame)
        self.cards_frame.pack()
        
        # Área de controles
        self.controls_frame = tk.Frame(self.main_frame)
        self.controls_frame.pack(pady=10)
        
        # Botão de sorteio
        self.draw_button = tk.Button(
            self.controls_frame,
            text="Sortear Número",
            command=self.request_number
        )
        self.draw_button.pack(side=tk.LEFT, padx=5)
        
        # Botão de Bingo
        self.bingo_button = tk.Button(
            self.controls_frame,
            text="BINGO!",
            command=self.claim_bingo
        )
        self.bingo_button.pack(side=tk.LEFT, padx=5)
        
        # Área de log
        self.log_text = scrolledtext.ScrolledText(
            self.main_frame,
            width=40,
            height=10
        )
        self.log_text.pack(pady=10)
    
    def create_card(self, numbers):
        """Cria uma nova cartela"""
        card = BingoCard(self.cards_frame, self.player_name, numbers)
        card.frame.pack(pady=5)
        self.card = card
    
    def handle_drawn_number(self, number):
        """Lida com um número sorteado"""
        if hasattr(self, 'card'):
            self.card.mark_drawn_number(number)
    
    def request_number(self):
        """Solicita um novo número ao servidor"""
        self.sio.emit('draw_number')
    
    def claim_bingo(self):
        """Clama vitória"""
        self.sio.emit('check_bingo')
    
    def log_message(self, message):
        """Adiciona uma mensagem ao log"""
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)
    
    def connect_to_server(self):
        """Conecta ao servidor"""
        try:
            self.sio.connect('http://localhost:8000')
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível conectar ao servidor: {e}")
            return False
    
    def start(self):
        """Inicia o jogo"""
        self.player_name = simpledialog.askstring("Nome", "Digite seu nome:")
        if not self.player_name:
            self.root.destroy()
            return
        
        if self.connect_to_server():
            self.sio.emit('join_game', self.player_name)
            self.root.mainloop()

if __name__ == "__main__":
    game = BingoGame()
    game.start()
