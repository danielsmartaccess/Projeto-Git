import tkinter as tk
from tkinter import messagebox
import random
from collections import Counter

class GeneralGame:
    def __init__(self, root):
        self.root = root
        self.root.title(" Jogo General - Edição Natalina ")
        self.root.configure(bg="#1c3144")  # Dark blue background
        
        # Variáveis do jogo
        self.dados = [0] * 5
        self.dados_selecionados = [False] * 5
        self.lancamentos_restantes = 3
        self.pontuacoes = {}
        self.rodada_atual = 1
        
        # Categorias de pontuação
        self.categorias = {
            "Ás": None, "Dois": None, "Três": None,
            "Quatro": None, "Cinco": None, "Seis": None,
            "Trinca": None, "Quadra": None, "Full House": None,
            "Sequência Menor": None, "Sequência Maior": None,
            "General": None, "Chance": None
        }
        
        # Interface
        self.criar_interface()
        
    def criar_interface(self):
        # Título decorativo
        titulo = tk.Label(self.root, text=" Jogo General ", 
                         font=("Helvetica", 24, "bold"), 
                         bg="#1c3144", fg="#e3b04b")  # Dourado natalino
        titulo.pack(pady=15)

        # Frame para os dados
        self.frame_dados = tk.Frame(self.root, bg="#1c3144")
        self.frame_dados.pack(pady=10)
        
        # Labels e Checkbuttons para os dados
        self.dados_labels = []
        self.dados_checks = []
        for i in range(5):
            frame = tk.Frame(self.frame_dados, bg="#1c3144")
            frame.pack(side=tk.LEFT, padx=10)
            
            label = tk.Label(frame, text="-", 
                           font=("Helvetica", 28, "bold"), 
                           width=2, 
                           bg="#2c4c63",  # Azul mais claro
                           fg="white",
                           relief="raised",
                           padx=10, pady=10)
            label.pack(pady=5)
            
            var = tk.BooleanVar()
            check = tk.Checkbutton(frame, text="Manter", 
                                 variable=var,
                                 command=lambda i=i: self.toggle_dado(i),
                                 bg="#1c3144",
                                 fg="white",
                                 selectcolor="#2c4c63",
                                 activebackground="#2c4c63",
                                 font=("Helvetica", 10))
            check.pack()
            
            self.dados_labels.append(label)
            self.dados_checks.append(var)
        
        # Botão de lançamento
        self.botao_lancar = tk.Button(self.root, 
                                    text=" Lançar Dados (3)", 
                                    command=self.lancar_dados,
                                    bg="#c41e3a",  # Vermelho natalino
                                    fg="white",
                                    font=("Helvetica", 12, "bold"),
                                    relief="raised",
                                    padx=20, pady=10)
        self.botao_lancar.pack(pady=15)
        
        # Frame para categorias e pontuação
        self.frame_score = tk.Frame(self.root, bg="#1c3144")
        self.frame_score.pack(pady=10, expand=True, fill=tk.BOTH)
        
        # Lista de categorias
        self.lista_categorias = tk.Listbox(self.frame_score, 
                                         height=13,
                                         font=("Helvetica", 11),
                                         bg="#2c4c63",
                                         fg="white",
                                         selectbackground="#e3b04b",
                                         selectforeground="black")
        for categoria in self.categorias:
            self.lista_categorias.insert(tk.END, categoria)
        self.lista_categorias.pack(side=tk.LEFT, padx=20, fill=tk.BOTH)
        
        # Frame para pontuações
        self.frame_pontuacoes = tk.Frame(self.frame_score, bg="#1c3144")
        self.frame_pontuacoes.pack(side=tk.LEFT, padx=20, fill=tk.BOTH)
        
        # Labels para pontuações
        self.labels_pontuacao = {}
        for categoria in self.categorias:
            frame = tk.Frame(self.frame_pontuacoes, bg="#1c3144")
            frame.pack(fill=tk.X, pady=2)
            tk.Label(frame, 
                    text=categoria + ":",
                    bg="#1c3144",
                    fg="white",
                    font=("Helvetica", 11)).pack(side=tk.LEFT)
            label = tk.Label(frame, 
                           text="-",
                           bg="#1c3144",
                           fg="#e3b04b",  # Dourado natalino
                           font=("Helvetica", 11, "bold"))
            label.pack(side=tk.RIGHT)
            self.labels_pontuacao[categoria] = label
        
        # Botão para marcar pontuação
        self.botao_marcar = tk.Button(self.root, 
                                    text=" Marcar Pontuação",
                                    command=self.marcar_pontos,
                                    bg="#2c8c3f",  # Verde natalino
                                    fg="white",
                                    font=("Helvetica", 12, "bold"),
                                    relief="raised",
                                    padx=20, pady=10)
        self.botao_marcar.pack(pady=15)
        
        # Frame para totais
        self.frame_totais = tk.Frame(self.root, bg="#1c3144")
        self.frame_totais.pack(pady=20)
        
        # Estilo comum para labels de totais
        label_style = {"bg": "#1c3144", "fg": "white", "font": ("Helvetica", 12)}
        
        self.label_superior = tk.Label(self.frame_totais, 
                                     text="Total Superior: 0",
                                     **label_style)
        self.label_superior.pack(pady=2)
        
        self.label_bonus = tk.Label(self.frame_totais, 
                                  text="Bônus: 0",
                                  **label_style)
        self.label_bonus.pack(pady=2)
        
        self.label_inferior = tk.Label(self.frame_totais, 
                                     text="Total Inferior: 0",
                                     **label_style)
        self.label_inferior.pack(pady=2)
        
        self.label_total = tk.Label(self.frame_totais, 
                                  text="Total Final: 0",
                                  font=("Helvetica", 14, "bold"),
                                  bg="#1c3144",
                                  fg="#e3b04b")  # Dourado natalino
        self.label_total.pack(pady=5)
        
        # Label para rodada atual
        self.label_rodada = tk.Label(self.root, text="Rodada: 1/13",
                                    bg="#1c3144",
                                    fg="white",
                                    font=("Helvetica", 12))
        self.label_rodada.pack(pady=5)

        # Criar menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu Ajuda
        ajuda_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=ajuda_menu)
        ajuda_menu.add_command(label="Regras", command=self.mostrar_regras)
        
    def toggle_dado(self, index):
        self.dados_selecionados[index] = self.dados_checks[index].get()

    def lancar_dados(self):
        if self.lancamentos_restantes <= 0:
            messagebox.showinfo("Aviso", "Você deve escolher uma categoria antes de lançar novamente!")
            return
        
        for i in range(5):
            if not self.dados_selecionados[i]:
                self.dados[i] = random.randint(1, 6)
                self.dados_labels[i].config(text=str(self.dados[i]))
        
        self.lancamentos_restantes -= 1
        self.botao_lancar.config(text=f" Lançar Dados ({self.lancamentos_restantes})")
        
        if self.lancamentos_restantes == 0:
            self.botao_lancar.config(state=tk.DISABLED)

    def calcular_pontuacao(self, categoria):
        contador = Counter(self.dados)
        
        if categoria in ["Ás", "Dois", "Três", "Quatro", "Cinco", "Seis"]:
            valor = {"Ás": 1, "Dois": 2, "Três": 3, "Quatro": 4, "Cinco": 5, "Seis": 6}[categoria]
            return sum(d for d in self.dados if d == valor)
        
        elif categoria == "Trinca":
            return sum(self.dados) if max(contador.values()) >= 3 else 0
        
        elif categoria == "Quadra":
            return sum(self.dados) if max(contador.values()) >= 4 else 0
        
        elif categoria == "Full House":
            return 25 if 2 in contador.values() and 3 in contador.values() else 0
        
        elif categoria == "Sequência Menor":
            dados_ordenados = sorted(set(self.dados))
            for i in range(len(dados_ordenados)-3):
                if dados_ordenados[i:i+4] == list(range(dados_ordenados[i], dados_ordenados[i]+4)):
                    return 30
            return 0
        
        elif categoria == "Sequência Maior":
            return 40 if len(set(self.dados)) == 5 and max(self.dados) - min(self.dados) == 4 else 0
        
        elif categoria == "General":
            return 50 if len(set(self.dados)) == 1 else 0
        
        elif categoria == "Chance":
            return sum(self.dados)
        
        return 0

    def marcar_pontos(self):
        if not self.lista_categorias.curselection():
            messagebox.showinfo("Aviso", "Selecione uma categoria!")
            return
            
        categoria = self.lista_categorias.get(self.lista_categorias.curselection())
        
        if self.categorias[categoria] is not None:
            messagebox.showinfo("Aviso", "Esta categoria já foi preenchida!")
            return
            
        pontos = self.calcular_pontuacao(categoria)
        self.categorias[categoria] = pontos
        self.labels_pontuacao[categoria].config(text=str(pontos))
        
        # Resetar para próxima rodada
        self.lancamentos_restantes = 3
        self.botao_lancar.config(text=" Lançar Dados (3)", state=tk.NORMAL)
        for i in range(5):
            self.dados_selecionados[i] = False
            self.dados_checks[i].set(False)
        
        self.rodada_atual += 1
        self.label_rodada.config(text=f"Rodada: {self.rodada_atual}/13")
        
        self.atualizar_pontuacao_total()
        
        if self.rodada_atual > 13:
            self.fim_de_jogo()

    def atualizar_pontuacao_total(self):
        # Calcular total superior
        superior = sum(self.categorias[cat] or 0 for cat in ["Ás", "Dois", "Três", "Quatro", "Cinco", "Seis"])
        bonus = 35 if superior >= 63 else 0
        
        # Calcular total inferior
        inferior = sum(self.categorias[cat] or 0 for cat in ["Trinca", "Quadra", "Full House", 
                                                           "Sequência Menor", "Sequência Maior",
                                                           "General", "Chance"])
        
        total = superior + bonus + inferior
        
        # Atualizar labels
        self.label_superior.config(text=f"Total Superior: {superior}")
        self.label_bonus.config(text=f"Bônus: {bonus}")
        self.label_inferior.config(text=f"Total Inferior: {inferior}")
        self.label_total.config(text=f"Total Final: {total}")

    def mostrar_regras(self):
        regras = """REGRAS DO JOGO GENERAL

OBJETIVO:
Somar o maior número de pontos possíveis em 13 rodadas.

COMO JOGAR:
- Em cada rodada, você tem 3 chances para lançar os dados
- Após cada lançamento, você pode segurar dados específicos
- Escolha uma categoria para pontuar após seus lançamentos

PONTUAÇÃO:
Parte Superior:
- Ás a Seis: Some apenas os dados do número escolhido
- Bônus de 35 pontos se somar 63 ou mais pontos

Parte Inferior:
- Trinca: 3 dados iguais (soma todos os dados)
- Quadra: 4 dados iguais (soma todos os dados)
- Full House: 3 de um número + 2 de outro (25 pontos)
- Sequência Menor: 4 dados em sequência (30 pontos)
- Sequência Maior: 5 dados em sequência (40 pontos)
- General: 5 dados iguais (50 pontos)
- Chance: Soma de todos os dados

Cada categoria só pode ser usada uma vez!"""
        
        messagebox.showinfo("Regras do Jogo", regras)

    def fim_de_jogo(self):
        # Calcular pontuação final
        superior = sum(self.categorias[cat] or 0 for cat in ["Ás", "Dois", "Três", "Quatro", "Cinco", "Seis"])
        bonus = 35 if superior >= 63 else 0
        inferior = sum(self.categorias[cat] or 0 for cat in ["Trinca", "Quadra", "Full House", 
                                                           "Sequência Menor", "Sequência Maior",
                                                           "General", "Chance"])
        total = superior + bonus + inferior
        
        mensagem = f"""Fim de Jogo!

Pontuação Final:
Total Superior: {superior}
Bônus: {bonus}
Total Inferior: {inferior}
Total Final: {total}

Obrigado por jogar!"""
        
        messagebox.showinfo("Fim de Jogo", mensagem)
        self.botao_lancar.config(state=tk.DISABLED)
        self.botao_marcar.config(state=tk.DISABLED)

# Executar o jogo
if __name__ == "__main__":
    root = tk.Tk()
    game = GeneralGame(root)
    root.mainloop()