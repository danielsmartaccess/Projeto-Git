import tkinter as tk
from tkinter import messagebox
import random
import time

class Minesweeper:
    def __init__(self, master):
        self.master = master
        self.master.title("Campo Minado")
        self.mines = 10  # Número de minas
        self.grid_size = 9  # Tamanho do grid 9x9
        self.buttons = {}
        self.mines_positions = set()
        self.flags = set()
        self.game_over = False
        self.time_count = 0
        self.timer_running = False
        
        # Cores personalizadas
        self.revealed_color = "#E8F4F9"  # Azul muito claro e suave
        self.number_colors = {
            1: "#0000FF",  # Azul
            2: "#008000",  # Verde
            3: "#FF0000",  # Vermelho
            4: "#000080",  # Azul escuro
            5: "#800000",  # Vermelho escuro
            6: "#008080",  # Ciano
            7: "#000000",  # Preto
            8: "#808080"   # Cinza
        }
        
        # Criar frame para controles
        self.control_frame = tk.Frame(master)
        self.control_frame.pack(pady=5)
        
        # Criar timer label com fonte maior
        self.timer_label = tk.Label(self.control_frame, text="Tempo: 0", font=('Arial', 28))
        self.timer_label.pack(side=tk.LEFT, padx=10)
        
        # Criar botão de reiniciar com fonte maior
        self.restart_button = tk.Button(self.control_frame, text="Novo Jogo", 
                                      command=self.restart_game, font=('Arial', 28))
        self.restart_button.pack(side=tk.LEFT, padx=10)
        
        # Criar frame principal
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Criar grid de botões
        self.create_board()
        # Distribuir minas
        self.place_mines()
        # Iniciar timer
        self.start_timer()

    def update_timer(self):
        if self.timer_running:
            self.time_count += 1
            self.timer_label.config(text=f"Tempo: {self.time_count}")
            self.master.after(1000, self.update_timer)

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def restart_game(self):
        # Parar o timer
        self.stop_timer()
        
        # Resetar variáveis
        self.time_count = 0
        self.timer_label.config(text="Tempo: 0")
        self.mines_positions.clear()
        self.flags.clear()
        self.game_over = False
        
        # Limpar e recriar o tabuleiro
        for button in self.buttons.values():
            button.destroy()
        self.buttons.clear()
        
        # Recriar o jogo
        self.create_board()
        self.place_mines()
        
        # Reiniciar o timer
        self.start_timer()

    def create_board(self):
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                button = tk.Button(
                    self.frame,
                    width=2,
                    height=1,
                    font=('Arial', 28),  # Fonte maior
                    command=lambda x=x, y=y: self.click(x, y)
                )
                button.grid(row=x, column=y)
                button.bind('<Button-3>', lambda e, x=x, y=y: self.place_flag(x, y))
                self.buttons[(x, y)] = button

    def place_mines(self):
        positions = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size)]
        self.mines_positions = set(random.sample(positions, self.mines))

    def get_neighbors(self, x, y):
        neighbors = []
        for i in range(max(0, x-1), min(self.grid_size, x+2)):
            for j in range(max(0, y-1), min(self.grid_size, y+2)):
                if (i, j) != (x, y):
                    neighbors.append((i, j))
        return neighbors

    def count_adjacent_mines(self, x, y):
        count = 0
        for nx, ny in self.get_neighbors(x, y):
            if (nx, ny) in self.mines_positions:
                count += 1
        return count

    def click(self, x, y):
        if self.game_over or (x, y) in self.flags:
            return

        button = self.buttons[(x, y)]
        
        if (x, y) in self.mines_positions:
            # Game Over
            button.configure(bg='red', text='💣', font=('Arial', 28))
            self.reveal_all_mines()
            self.game_over = True
            self.stop_timer()
            messagebox.showinfo("Game Over", f"Você perdeu! Tempo: {self.time_count} segundos")
            return

        self.reveal_cell(x, y)
        
        # Verificar vitória
        if self.check_win():
            self.stop_timer()
            messagebox.showinfo("Parabéns", f"Você venceu! Tempo: {self.time_count} segundos")
            self.game_over = True

    def reveal_cell(self, x, y):
        if (x, y) not in self.buttons or \
           self.buttons[(x, y)]['state'] == 'disabled':
            return

        button = self.buttons[(x, y)]
        mines = self.count_adjacent_mines(x, y)
        
        button.configure(
            state='disabled',
            relief='sunken',
            bg=self.revealed_color  # Cor de fundo para células reveladas
        )
        
        if mines > 0:
            button.configure(
                text=str(mines),
                fg=self.number_colors.get(mines, 'black')  # Cor do número
            )
        else:
            button.configure(text='')
            # Revelar células vizinhas se não houver minas adjacentes
            for nx, ny in self.get_neighbors(x, y):
                self.reveal_cell(nx, ny)

    def place_flag(self, x, y):
        if self.game_over:
            return
        
        if (x, y) not in self.flags and len(self.flags) < self.mines:
            self.buttons[(x, y)].configure(text='🚩', font=('Arial', 28))
            self.flags.add((x, y))
        elif (x, y) in self.flags:
            self.buttons[(x, y)].configure(text='')
            self.flags.remove((x, y))

    def reveal_all_mines(self):
        for x, y in self.mines_positions:
            if (x, y) not in self.flags:
                self.buttons[(x, y)].configure(text='💣', bg='red', font=('Arial', 28))

    def check_win(self):
        revealed_count = sum(1 for button in self.buttons.values() 
                           if button['state'] == 'disabled')
        return revealed_count == (self.grid_size * self.grid_size - self.mines)

def new_game():
    root = tk.Tk()
    Minesweeper(root)
    root.mainloop()

if __name__ == '__main__':
    new_game()
