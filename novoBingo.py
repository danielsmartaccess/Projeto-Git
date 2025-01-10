import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

class CartelaBingo:
    def __init__(self, master):
        """
        Inicializa a interface da cartela de Bingo.

        Args:
            master: Janela principal do Tkinter.
        """
        self.master = master
        self.master.title("Bingo Game - SENAC")
        
        # Frame para o logo
        self.frame_logo = tk.Frame(master)
        self.frame_logo.pack(pady=10)
        
        # Carregar e exibir o logo
        self.carregar_logo()
        
        # Configuração do layout principal
        self.frame_principal = tk.Frame(master)
        self.frame_principal.pack(padx=10, pady=10)
        
        # Frame para cartela
        self.frame_cartela = tk.Frame(self.frame_principal)
        self.frame_cartela.pack(side=tk.LEFT, padx=10)
        
        # Frame para controles e números sorteados
        self.frame_controles = tk.Frame(self.frame_principal)
        self.frame_controles.pack(side=tk.LEFT, padx=10)
        
        # Inicialização de variáveis
        self.numeros_sorteados = []
        self.labels_numeros = {}
        self.numeros_cartela = {}
        
        # Criar elementos da interface
        self.criar_cartela()
        self.criar_controles()
        
    def carregar_logo(self):
        """
        Carrega e exibe o logo do Senac
        """
        try:
            # Carregar a imagem
            logo_path = os.path.join(os.path.dirname(__file__), "logo_senac.png")
            imagem_original = Image.open(logo_path)
            
            # Calcular nova altura mantendo a proporção
            largura_desejada = 200  # Largura desejada em pixels
            proporcao = largura_desejada / imagem_original.width
            altura_nova = int(imagem_original.height * proporcao)
            
            # Redimensionar mantendo a proporção
            imagem_redimensionada = imagem_original.resize((largura_desejada, altura_nova), Image.Resampling.LANCZOS)
            
            # Converter para formato Tkinter
            self.logo_img = ImageTk.PhotoImage(imagem_redimensionada)
            
            # Criar e exibir label com o logo
            logo_label = tk.Label(self.frame_logo, image=self.logo_img)
            logo_label.pack()
        except Exception as e:
            print(f"Erro ao carregar o logo: {e}")
            
    def criar_cartela(self):
        """
        Gera a cartela de Bingo com números aleatórios e exibe na interface.
        """
        colunas = {
            'B': random.sample(range(1, 16), 5),
            'I': random.sample(range(16, 31), 5),
            'N': random.sample(range(31, 46), 5),
            'G': random.sample(range(46, 61), 5),
            'O': random.sample(range(61, 76), 5)
        }

        # Espaço central "LIVRE"
        colunas['N'][2] = "LIVRE"

        # Exibir as letras BINGO
        for idx, letra in enumerate("BINGO"):
            tk.Label(self.frame_cartela, text=letra, font=('Helvetica', 16, 'bold')).grid(row=0, column=idx)

        # Exibir os números
        for col_idx, letra in enumerate("BINGO"):
            for row_idx, numero in enumerate(colunas[letra]):
                label = tk.Label(
                    self.frame_cartela,
                    text=numero,
                    font=('Helvetica', 14),
                    width=5,
                    height=2,
                    borderwidth=2,
                    relief="groove",
                    bg='white'
                )
                label.grid(row=row_idx + 1, column=col_idx)
                if numero != "LIVRE":
                    self.labels_numeros[numero] = label
                    self.numeros_cartela[numero] = False

    def criar_controles(self):
        """
        Cria os controles do jogo e área de exibição dos números sorteados.
        """
        # Botão de sorteio
        self.btn_sortear = tk.Button(
            self.frame_controles,
            text="Sortear Número",
            command=self.sortear_numero,
            font=('Helvetica', 12),
            bg='lightblue'
        )
        self.btn_sortear.pack(pady=10)

        # Label para último número sorteado
        self.lbl_ultimo_sorteado = tk.Label(
            self.frame_controles,
            text="Último número:",
            font=('Helvetica', 12)
        )
        self.lbl_ultimo_sorteado.pack(pady=5)

        # Frame para lista de números sorteados
        self.frame_numeros = tk.Frame(self.frame_controles)
        self.frame_numeros.pack(pady=10)
        
        tk.Label(
            self.frame_numeros,
            text="Números Sorteados:",
            font=('Helvetica', 12)
        ).pack()

        # Lista de números sorteados
        self.lista_sorteados = tk.Listbox(
            self.frame_numeros,
            width=20,
            height=10,
            font=('Helvetica', 10)
        )
        self.lista_sorteados.pack()

    def sortear_numero(self):
        """
        Sorteia um novo número e atualiza a interface.
        """
        # Verificar se ainda há números disponíveis para sorteio
        numeros_disponiveis = set(range(1, 76)) - set(self.numeros_sorteados)
        
        if not numeros_disponiveis:
            messagebox.showinfo("Fim do Jogo", "Todos os números já foram sorteados!")
            return

        # Sortear novo número
        numero = random.choice(list(numeros_disponiveis))
        self.numeros_sorteados.append(numero)
        
        # Atualizar último número sorteado
        self.lbl_ultimo_sorteado.config(text=f"Último número: {numero}")
        
        # Adicionar à lista de sorteados
        self.lista_sorteados.insert(0, str(numero))
        
        # Marcar número na cartela se presente
        if numero in self.labels_numeros:
            self.labels_numeros[numero].config(bg='lightgreen')
            self.numeros_cartela[numero] = True
            
            # Verificar vitória
            if self.verificar_vitoria():
                messagebox.showinfo("BINGO!", "Parabéns! Você completou a cartela!")
                self.btn_sortear.config(state='disabled')

    def verificar_vitoria(self):
        """
        Verifica se todos os números da cartela foram marcados.
        """
        return all(self.numeros_cartela.values())

# Inicialização do jogo
if __name__ == "__main__":
    root = tk.Tk()
    app = CartelaBingo(root)
    root.mainloop()
