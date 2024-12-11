import tkinter as tk
from tkinter import ttk, messagebox
import random
from PIL import Image, ImageTk
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = {}
        self.total_score = 0

    def add_score(self, combination, points):
        self.scores[combination] = points
        self.total_score = sum(self.scores.values())

class GeneralGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Casino General - Multiplayer")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a1a')

        # Variáveis do jogo
        self.players = []
        self.current_player_index = 0
        self.dice_values = [1, 1, 1, 1, 1]
        self.dice_locked = [False] * 5
        self.rolls_left = 3
        self.current_round = 0
        self.score_buttons = {}
        self.current_attempt = 1
        
        # Criar diretório para imagens se não existir
        if not os.path.exists('dice_images'):
            os.makedirs('dice_images')

        # Primeiro, mostrar tela de registro de jogadores
        self.show_player_registration()

    def show_player_registration(self):
        # Limpar janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Frame de registro
        register_frame = tk.Frame(self.root, bg='#1a1a1a')
        register_frame.pack(expand=True)

        # Título
        title = tk.Label(register_frame,
                        text="🎲 Casino General - Registro de Jogadores 🎲",
                        font=("Arial", 24, "bold"),
                        bg='#1a1a1a',
                        fg='gold')
        title.pack(pady=20)

        # Instruções
        instructions = tk.Label(register_frame,
                              text="Registre de 2 a 4 jogadores",
                              font=("Arial", 12),
                              bg='#1a1a1a',
                              fg='white')
        instructions.pack(pady=10)

        # Entradas para nomes
        self.player_entries = []
        for i in range(4):
            frame = tk.Frame(register_frame, bg='#1a1a1a')
            frame.pack(pady=5)
            
            label = tk.Label(frame,
                           text=f"Jogador {i+1}:",
                           font=("Arial", 12),
                           bg='#1a1a1a',
                           fg='white')
            label.pack(side=tk.LEFT, padx=5)
            
            entry = tk.Entry(frame, font=("Arial", 12))
            entry.pack(side=tk.LEFT, padx=5)
            self.player_entries.append(entry)

        # Botão de início
        start_button = tk.Button(register_frame,
                               text="Iniciar Jogo",
                               command=self.start_game,
                               font=("Arial", 14, "bold"),
                               bg='gold',
                               fg='black',
                               padx=20,
                               pady=10)
        start_button.pack(pady=20)

    def start_game(self):
        # Validar jogadores
        player_names = [entry.get().strip() for entry in self.player_entries if entry.get().strip()]
        
        if len(player_names) < 2:
            messagebox.showerror("Erro", "É necessário pelo menos 2 jogadores!")
            return
        
        # Criar jogadores
        self.players = [Player(name) for name in player_names]
        
        # Criar imagens dos dados
        self.create_dice_images()
        
        # Configurar interface do jogo
        self.setup_ui()

    def setup_ui(self):
        # Limpar janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Configurar estilo
        style = ttk.Style()
        style.configure('Casino.TFrame', background='#1a1a1a')
        style.configure('Casino.TButton', 
                       background='gold',
                       foreground='black',
                       font=('Arial', 10, 'bold'),
                       padding=5)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(expand=True, fill='both')

        # Frame de jogadores (lado esquerdo)
        players_frame = tk.Frame(main_frame, bg='#2a2a2a', width=200)
        players_frame.pack(side=tk.LEFT, fill='y', padx=10, pady=10)
        
        # Placar dos jogadores
        tk.Label(players_frame,
                text="Placar",
                font=("Arial", 16, "bold"),
                bg='#2a2a2a',
                fg='gold').pack(pady=10)

        self.player_labels = []
        for player in self.players:
            label = tk.Label(players_frame,
                           text=f"{player.name}: 0",
                           font=("Arial", 12),
                           bg='#2a2a2a',
                           fg='white')
            label.pack(pady=5)
            self.player_labels.append(label)

        # Frame de jogo (centro)
        game_frame = tk.Frame(main_frame, bg='#1a1a1a')
        game_frame.pack(side=tk.LEFT, expand=True, fill='both')

        # Jogador atual
        self.current_player_label = tk.Label(game_frame,
                                           text=f"Vez de: {self.players[0].name}",
                                           font=("Arial", 20, "bold"),
                                           bg='#1a1a1a',
                                           fg='gold')
        self.current_player_label.pack(pady=10)

        # Informações do jogo
        info_frame = tk.Frame(game_frame, bg='#1a1a1a')
        info_frame.pack(pady=10)
        
        self.attempt_label = tk.Label(info_frame,
                                    text="Tentativa 1 de 3",
                                    font=("Arial", 12),
                                    bg='#1a1a1a',
                                    fg='white')
        self.attempt_label.pack()
        
        self.rolls_label = tk.Label(info_frame,
                                  text="Jogadas restantes: 3",
                                  font=("Arial", 12),
                                  bg='#1a1a1a',
                                  fg='white')
        self.rolls_label.pack()

        instructions = tk.Label(info_frame,
                              text="Clique nos dados para preservá-los na próxima jogada",
                              font=("Arial", 10, "italic"),
                              bg='#1a1a1a',
                              fg='#aaaaaa')
        instructions.pack(pady=5)

        # Frame para os dados
        self.dice_frame = tk.Frame(game_frame, bg='#0a5c0a', padx=20, pady=20)
        self.dice_frame.pack(pady=20)

        # Criar botões dos dados
        self.dice_buttons = []
        for i in range(5):
            btn = tk.Button(self.dice_frame,
                          image=self.dice_images[0],
                          command=lambda x=i: self.toggle_lock(x),
                          relief=tk.RAISED,
                          bg='white',
                          activebackground='#ffcccc')
            btn.grid(row=0, column=i, padx=10)
            self.dice_buttons.append(btn)

        # Botão de jogar
        self.roll_button = tk.Button(game_frame,
                                   text="🎲 Jogar Dados 🎲",
                                   command=self.roll_dice,
                                   font=("Arial", 14, "bold"),
                                   bg='gold',
                                   fg='black',
                                   relief=tk.RAISED,
                                   padx=20,
                                   pady=10)
        self.roll_button.pack(pady=20)

        # Frame para pontuação
        score_frame = tk.Frame(game_frame, bg='#2a2a2a', padx=20, pady=10)
        score_frame.pack(pady=20, padx=20, fill='x')

        score_title = tk.Label(score_frame,
                             text="Combinações Disponíveis",
                             font=("Arial", 14, "bold"),
                             bg='#2a2a2a',
                             fg='gold')
        score_title.pack(pady=(0, 10))

        # Grid para as opções de pontuação
        button_frame = tk.Frame(score_frame, bg='#2a2a2a')
        button_frame.pack()

        score_options = {
            'Uns 🎯': self.score_ones,
            'Dois 🎯': self.score_twos,
            'Três 🎯': self.score_threes,
            'Quatros 🎯': self.score_fours,
            'Cincos 🎯': self.score_fives,
            'Seis 🎯': self.score_sixes,
            'Sequência Baixa 🔄': self.score_low_straight,
            'Sequência Alta 🔄': self.score_high_straight,
            'Full Hand 🃏': self.score_full_house,
            'Poker 🎰': self.score_poker,
            'General ⭐': self.score_general
        }

        row = 0
        col = 0
        for name, func in score_options.items():
            btn = tk.Button(button_frame,
                          text=f"{name}: --",
                          command=lambda f=func, n=name: self.score_combination(f, n),
                          width=20,
                          height=2,
                          font=("Arial", 10, "bold"),
                          bg='#3a3a3a',
                          fg='white',
                          relief=tk.RAISED)
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.score_buttons[name] = btn
            col += 1
            if col > 2:
                col = 0
                row += 1

    def update_player_labels(self):
        for i, player in enumerate(self.players):
            text = f"{player.name}: {player.total_score}"
            if i == self.current_player_index:
                text += " 👉"
            self.player_labels[i].configure(text=text)

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player_label.configure(text=f"Vez de: {self.players[self.current_player_index].name}")
        self.update_player_labels()
        self.reset_round()

    def score_combination(self, score_func, name):
        current_player = self.players[self.current_player_index]
        if name not in current_player.scores:
            points = score_func()
            current_player.add_score(name, points)
            self.score_buttons[name].configure(
                text=f"{name}: {points}",
                state=tk.DISABLED,
                bg='#444444'
            )
            
            self.update_player_labels()
            
            # Verificar fim do jogo
            if all(len(p.scores) == 11 for p in self.players):
                self.show_final_scores()
            else:
                self.next_player()

    def show_final_scores(self):
        # Ordenar jogadores por pontuação
        sorted_players = sorted(self.players, key=lambda x: x.total_score, reverse=True)
        
        # Criar mensagem com ranking
        message = "🏆 Fim do Jogo! 🏆\n\nRanking:\n"
        for i, player in enumerate(sorted_players, 1):
            message += f"{i}º lugar: {player.name} - {player.total_score} pontos\n"
        
        messagebox.showinfo("Fim do Jogo", message)
        self.root.quit()

    def create_dice_images(self):
        # Gerar as imagens dos dados
        import dice_generator
        dice_generator.generate_dice_images()
        
        # Carregar as imagens dos dados
        self.dice_images = []
        for i in range(1, 7):
            img = Image.open(f'dice_images/dice_{i}.png')
            self.dice_images.append(ImageTk.PhotoImage(img))

    def toggle_lock(self, index):
        if self.rolls_left < 3:  # Só pode travar após primeira jogada
            self.dice_locked[index] = not self.dice_locked[index]
            color = '#ffcccc' if self.dice_locked[index] else 'white'
            self.dice_buttons[index].configure(bg=color)
            # Adicionar efeito de brilho quando travado
            if self.dice_locked[index]:
                self.dice_buttons[index].configure(relief=tk.SUNKEN)
            else:
                self.dice_buttons[index].configure(relief=tk.RAISED)

    def roll_dice(self):
        if self.rolls_left > 0:
            for i in range(5):
                if not self.dice_locked[i]:
                    self.dice_values[i] = random.randint(1, 6)
                    # Atualizar visual do dado
                    self.dice_buttons[i].configure(image=self.dice_images[self.dice_values[i]-1])
            
            self.rolls_left -= 1
            self.rolls_label.configure(text=f"Jogadas restantes: {self.rolls_left}")
            
            if self.rolls_left == 0:
                self.roll_button.configure(state=tk.DISABLED)
                # Perguntar se quer manter esta jogada ou tentar novamente
                if self.current_attempt < 3:
                    self.ask_keep_or_retry()
        else:
            messagebox.showinfo("Aviso", "Você deve escolher uma combinação!")

    def ask_keep_or_retry(self):
        response = messagebox.askyesno("Tentar Novamente?",
                                     "Deseja manter esta jogada?\n\n" +
                                     "Sim - Manter esta jogada\n" +
                                     "Não - Tentar novamente")
        if response:  # Manter a jogada
            self.enable_scoring_buttons()
        else:  # Tentar novamente
            self.current_attempt += 1
            self.reset_round(keep_score_buttons=True)
            self.attempt_label.configure(text=f"Tentativa {self.current_attempt} de 3")

    def reset_round(self, keep_score_buttons=False):
        self.rolls_left = 3
        self.dice_locked = [False] * 5
        self.roll_button.configure(state=tk.NORMAL)
        
        # Resetar visual dos dados
        for btn in self.dice_buttons:
            btn.configure(bg='white', relief=tk.RAISED)
        
        if not keep_score_buttons:
            self.current_attempt = 1
            self.attempt_label.configure(text="Tentativa 1 de 3")

    def enable_scoring_buttons(self):
        # Habilitar botões de pontuação que ainda não foram usados
        for name, btn in self.score_buttons.items():
            if name not in self.players[self.current_player_index].scores:
                btn.configure(state=tk.NORMAL)

    def count_values(self):
        counts = [0] * 7
        for value in self.dice_values:
            counts[value] += 1
        return counts

    # Funções de pontuação
    def score_number(self, number):
        return sum(d for d in self.dice_values if d == number)

    def score_ones(self): return self.score_number(1)
    def score_twos(self): return self.score_number(2)
    def score_threes(self): return self.score_number(3)
    def score_fours(self): return self.score_number(4)
    def score_fives(self): return self.score_number(5)
    def score_sixes(self): return self.score_number(6)

    def score_low_straight(self):
        return 15 if sorted(self.dice_values) == [1,2,3,4,5] else 0

    def score_high_straight(self):
        return 20 if sorted(self.dice_values) == [2,3,4,5,6] else 0

    def score_full_house(self):
        counts = self.count_values()
        if 2 in counts and 3 in counts:
            return 25
        return 0

    def score_poker(self):
        counts = self.count_values()
        if 4 in counts:
            return 30
        return 0

    def score_general(self):
        if len(set(self.dice_values)) == 1:
            return 50
        return 0

if __name__ == "__main__":
    root = tk.Tk()
    game = GeneralGame(root)
    root.mainloop()
