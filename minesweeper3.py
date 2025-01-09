# =================================================================
# Campo Minado (Minesweeper) - Implementação com Interface Gráfica
# =================================================================
"""
Este é um jogo de Campo Minado implementado em Python usando Tkinter.
O jogo possui as seguintes características:
- Interface gráfica interativa
- Sistema de marcação de minas com bandeiras
- Contador de tempo
- Logo do SENAC no título
"""

# Importação das bibliotecas necessárias
import tkinter as tk              # Interface gráfica
from tkinter import messagebox    # Caixas de diálogo
import random                     # Geração de números aleatórios
import time                       # Controle de tempo
from PIL import Image, ImageTk    # Manipulação de imagens

# =================================================================
# Classe Cell: Representa uma célula individual do tabuleiro
# =================================================================
class Cell:
    def __init__(self):
        """
        Inicializa uma célula com seus atributos básicos:
        - has_mine: Indica se contém uma mina
        - adjacent_mines: Quantidade de minas adjacentes
        - state: Estado atual ('hidden', 'revealed' ou 'flagged')
        """
        self.has_mine = False
        self.adjacent_mines = 0
        self.state = "hidden"

# =================================================================
# Classe Grid: Gerencia o tabuleiro e a lógica do jogo
# =================================================================
class Grid:
    def __init__(self, rows, cols, num_mines):
        """
        Inicializa o tabuleiro do jogo.
        
        Parâmetros:
        - rows: Número de linhas
        - cols: Número de colunas
        - num_mines: Quantidade de minas
        """
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        # Cria matriz 2D de células
        self.board = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.mines_positions = []

    def generate_mines(self, first_click):
        """
        Distribui as minas aleatoriamente pelo tabuleiro.
        Garante que a primeira célula clicada não contenha mina.
        
        Parâmetros:
        - first_click: Tupla (row, col) da primeira célula clicada
        """
        all_positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        all_positions.remove(first_click)  # Remove posição do primeiro clique
        self.mines_positions = random.sample(all_positions, self.num_mines)
        
        # Coloca as minas nas posições sorteadas
        for r, c in self.mines_positions:
            self.board[r][c].has_mine = True

    def calculate_adjacencies(self):
        """
        Calcula o número de minas adjacentes para cada célula.
        Usa as 8 direções possíveis (horizontal, vertical e diagonal).
        """
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Superior
            ( 0, -1),          ( 0, 1),  # Laterais
            ( 1, -1), ( 1, 0), ( 1, 1)   # Inferior
        ]
        
        # Percorre cada célula do tabuleiro
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.board[r][c].has_mine:
                    # Conta minas nas células adjacentes
                    count = 0
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if (0 <= new_r < self.rows and 
                            0 <= new_c < self.cols and 
                            self.board[new_r][new_c].has_mine):
                            count += 1
                    self.board[r][c].adjacent_mines = count

    def reveal_cell(self, row, col):
        """
        Revela uma célula e suas adjacentes se não houver minas próximas.
        
        Parâmetros:
        - row, col: Coordenadas da célula a ser revelada
        
        Retorna:
        - "game_over" se uma mina for revelada
        - None caso contrário
        """
        cell = self.board[row][col]
        if cell.state != "hidden" or cell.state == "flagged":
            return
            
        cell.state = "revealed"
        
        if cell.has_mine:
            return "game_over"
            
        # Se não há minas adjacentes, revela células vizinhas
        if cell.adjacent_mines == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    new_r, new_c = row + dr, col + dc
                    if (0 <= new_r < self.rows and 
                        0 <= new_c < self.cols):
                        self.reveal_cell(new_r, new_c)

    def check_victory(self):
        """
        Verifica se o jogador venceu.
        Vitória ocorre quando todas as células sem mina estão reveladas.
        """
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.board[r][c]
                if not cell.has_mine and cell.state != "revealed":
                    return False
        return True

    def mark_cell(self, row, col):
        """
        Marca/Desmarca uma célula com uma bandeira.
        
        Parâmetros:
        - row, col: Coordenadas da célula
        """
        cell = self.board[row][col]
        if cell.state == "hidden":
            cell.state = "flagged"
        elif cell.state == "flagged":
            cell.state = "hidden"

# =================================================================
# Classe MinesweeperApp: Interface Gráfica do Jogo
# =================================================================
class MinesweeperApp:
    def __init__(self, master):
        """
        Inicializa a interface gráfica do jogo.
        
        Parâmetros:
        - master: Janela principal do Tkinter
        """
        self.master = master
        self.master.title("Campo Minado - SENAC")
        
        # Configuração do logo no título
        title_image = Image.open("senac-logo-0.png")
        title_image = title_image.resize((150, 50), Image.Resampling.LANCZOS)
        self.title_photo = ImageTk.PhotoImage(title_image)
        
        # Criação dos elementos da interface
        self.title_logo = tk.Label(self.master, image=self.title_photo)
        self.title_logo.grid(row=0, column=0, columnspan=9, pady=10)
        
        # Inicialização do jogo
        self.grid = Grid(9, 9, 10)  # Tabuleiro 9x9 com 10 minas
        self.first_click = True
        self.buttons = []
        
        # Configuração do contador de tempo
        self.start_time = None
        self.timer_label = tk.Label(self.master, text="Tempo: 0s", font=("Arial", 12))
        self.timer_label.grid(row=1, column=0, columnspan=9)
        
        # Cria os botões do tabuleiro
        self.create_widgets()

    def create_widgets(self):
        """
        Cria os botões do tabuleiro.
        Cada botão é configurado com eventos de clique esquerdo e direito.
        """
        for r in range(self.grid.rows):
            row_buttons = []
            for c in range(self.grid.cols):
                btn = tk.Button(self.master, width=2, height=1, font=("Arial", 14, "bold"))
                btn.bind("<Button-1>", lambda event, r=r, c=c: self.on_left_click(r, c))
                btn.bind("<Button-3>", lambda event, r=r, c=c: self.on_right_click(r, c))
                btn.grid(row=r + 2, column=c)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def start_timer(self):
        """
        Inicia o contador de tempo no primeiro clique.
        """
        if self.start_time is None:
            self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        """
        Atualiza o contador de tempo a cada segundo.
        """
        if self.start_time is not None:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Tempo: {elapsed_time}s")
            self.master.after(1000, self.update_timer)

    def on_left_click(self, row, col):
        """
        Manipula o clique esquerdo do mouse (revelar célula).
        
        Parâmetros:
        - row, col: Coordenadas da célula clicada
        """
        if self.first_click:
            self.grid.generate_mines((row, col))
            self.grid.calculate_adjacencies()
            self.first_click = False
            self.start_timer()

        result = self.grid.reveal_cell(row, col)
        self.update_buttons()

        if result == "game_over":
            self.show_game_over()
        elif self.grid.check_victory():
            self.show_victory()

    def on_right_click(self, row, col):
        """
        Manipula o clique direito do mouse (marcar bandeira).
        
        Parâmetros:
        - row, col: Coordenadas da célula clicada
        """
        self.grid.mark_cell(row, col)
        self.update_buttons()

    def update_buttons(self):
        """
        Atualiza a aparência dos botões conforme o estado do jogo.
        Define cores diferentes para cada número de minas adjacentes.
        """
        number_colors = {
            1: 'blue',
            2: 'green',
            3: 'red',
            4: 'purple',
            5: 'maroon',
            6: 'turquoise',
            7: 'black',
            8: 'gray'
        }
        
        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                cell = self.grid.board[r][c]
                btn = self.buttons[r][c]
                if cell.state == "revealed":
                    if cell.has_mine:
                        btn.config(text="💣", bg="red")
                    else:
                        btn.config(bg="white")
                        if cell.adjacent_mines > 0:
                            btn.config(text=str(cell.adjacent_mines), 
                                     fg=number_colors.get(cell.adjacent_mines, 'black'))
                        else:
                            btn.config(text="")
                elif cell.state == "flagged":
                    btn.config(text="🚩", bg="yellow")
                else:
                    btn.config(text="", bg="SystemButtonFace")

    def show_game_over(self):
        """
        Exibe mensagem de derrota e reinicia o jogo.
        """
        messagebox.showinfo("Game Over", "Você perdeu! Tente novamente.")
        self.master.quit()

    def show_victory(self):
        """
        Exibe mensagem de vitória e reinicia o jogo.
        """
        messagebox.showinfo("Vitória", "Parabéns! Você venceu!")
        self.master.quit()

# =================================================================
# Inicialização do Jogo
# =================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = MinesweeperApp(root)
    root.mainloop()
