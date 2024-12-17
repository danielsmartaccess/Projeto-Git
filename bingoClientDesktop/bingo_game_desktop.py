import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import random
import os

class BingoCard:
    """Classe responsável por criar e gerenciar uma cartela de bingo individual"""
    
    def __init__(self, master, player_name, card_numbers):
        """
        Inicializa uma nova cartela de bingo
        
        Args:
            master: Widget pai do Tkinter
            player_name: Nome do jogador
            card_numbers: Lista com os números da cartela
        """
        self.frame = tk.LabelFrame(master, text=f"Cartela - {player_name}", padx=10, pady=5)
        self.numbers = sorted(card_numbers)  # Ordena os números em ordem crescente
        self.marked = set()  # Conjunto para armazenar números marcados
        self.buttons = []
        self._create_card()
    
    def _create_card(self):
        """Cria a interface gráfica da cartela com botões"""
        for i in range(4):  # Alterado para 4x4
            for j in range(4):
                index = i * 4 + j
                number = self.numbers[index]
                btn = tk.Button(
                    self.frame,
                    text=str(number),
                    width=4,
                    command=lambda n=number: self._mark_number(n)
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(btn)
    
    def _mark_number(self, number):
        """
        Marca um número na cartela
        
        Args:
            number: Número a ser marcado
        """
        if number in self.marked:
            self.marked.remove(number)
            self._update_button_color(number, "SystemButtonFace")
        else:
            self.marked.add(number)
            self._update_button_color(number, "light green")
    
    def _update_button_color(self, number, color):
        """
        Atualiza a cor do botão
        
        Args:
            number: Número do botão a ser atualizado
            color: Nova cor do botão
        """
        for btn in self.buttons:
            if btn["text"] == str(number):
                btn.configure(bg=color)
                break

class BingoGame:
    """Classe principal do jogo de Bingo"""
    
    def __init__(self):
        """Inicializa o jogo de Bingo"""
        self.root = tk.Tk()
        self.root.title("Jogo de Bingo")
        self.cards = []  # Lista para armazenar as cartelas
        self.drawn_numbers = []  # Lista para armazenar números sorteados na ordem
        self.drawn_numbers_set = set()  # Conjunto para verificação rápida
        self._setup_game()
    
    def _setup_game(self):
        """Configura a interface inicial do jogo"""
        # Frame para controles do jogo
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        # Botão para sortear número
        self.draw_button = tk.Button(
            control_frame,
            text="Sortear Número",
            command=self._draw_number
        )
        self.draw_button.pack(side=tk.LEFT, padx=5)
        
        # Label para mostrar o último número sorteado
        self.last_number_label = tk.Label(
            control_frame,
            text="Último número: -",
            font=("Arial", 12)
        )
        self.last_number_label.pack(side=tk.LEFT, padx=5)

        # Área de texto para mostrar todos os números sorteados
        self.drawn_numbers_text = scrolledtext.ScrolledText(
            self.root,
            width=40,
            height=4,
            wrap=tk.WORD
        )
        self.drawn_numbers_text.pack(pady=5)
        self.drawn_numbers_text.insert(tk.END, "Números sorteados: ")
        
        # Frame para as cartelas
        self.cards_frame = tk.Frame(self.root)
        self.cards_frame.pack(pady=10)
    
    def _generate_card_numbers(self):
        """
        Gera números aleatórios para uma cartela
        
        Returns:
            Lista com 16 números únicos entre 0 e 99
        """
        return random.sample(range(100), 16)  # Alterado para 16 números
    
    def _draw_number(self):
        """Sorteia um novo número"""
        available_numbers = set(range(100)) - self.drawn_numbers_set
        if not available_numbers:
            messagebox.showinfo("Fim do Jogo", "Todos os números já foram sorteados!")
            return
        
        number = random.choice(list(available_numbers))
        self.drawn_numbers.append(number)  # Adiciona à lista na ordem do sorteio
        self.drawn_numbers_set.add(number)  # Adiciona ao conjunto para verificação
        self.last_number_label.config(text=f"Último número: {number}")
        
        # Atualiza a lista de números sorteados mantendo a ordem do sorteio
        self.drawn_numbers_text.delete(1.0, tk.END)
        self.drawn_numbers_text.insert(tk.END, "Números sorteados: " + 
                                     ", ".join(map(str, self.drawn_numbers)))

    def start_game(self):
        """Inicia o jogo solicitando o número de jogadores"""
        num_players = simpledialog.askinteger(
            "Número de Jogadores",
            "Digite o número de jogadores:",
            minvalue=1,
            maxvalue=10
        )
        
        if not num_players:
            self.root.quit()
            return
        
        # Cria cartelas para cada jogador
        for i in range(num_players):
            card = BingoCard(
                self.cards_frame,
                f"Jogador {i+1}",
                self._generate_card_numbers()
            )
            card.frame.grid(row=i//2, column=i%2, padx=10, pady=5)
            self.cards.append(card)
        
        self.root.mainloop()

if __name__ == "__main__":
    game = BingoGame()
    game.start_game()
