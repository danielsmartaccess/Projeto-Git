import tkinter as tk
from tkinter import messagebox
import random

class BingoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo 4x4 🎲")
        self.root.configure(bg='#f0f0f0')
        
        # Configurações do jogo
        self.numeros_disponiveis = list(range(1, 76))  # Números de 1 a 75
        self.numeros_sorteados = []
        self.cartela = []
        self.premios_ganhos = []
        
        # Criar e configurar a cartela
        self.criar_cartela()
        self.criar_interface()
        
    def criar_cartela(self):
        # Gerar 16 números aleatórios para a cartela 4x4
        self.cartela = random.sample(self.numeros_disponiveis, 16)
        self.cartela_matrix = [self.cartela[i:i+4] for i in range(0, 16, 4)]
        
    def criar_interface(self):
        # Frame principal
        self.frame_principal = tk.Frame(self.root, bg='#f0f0f0')
        self.frame_principal.pack(padx=20, pady=20)
        
        # Título
        titulo = tk.Label(self.frame_principal, text="BINGO 4x4", font=('Arial', 24, 'bold'), bg='#f0f0f0')
        titulo.pack(pady=10)
        
        # Frame para a cartela
        self.frame_cartela = tk.Frame(self.frame_principal, bg='#f0f0f0')
        self.frame_cartela.pack()
        
        # Criar botões da cartela
        self.botoes = []
        for i in range(4):
            for j in range(4):
                numero = self.cartela_matrix[i][j]
                btn = tk.Button(self.frame_cartela, text=str(numero), width=5, height=2,
                              font=('Arial', 14), command=lambda x=numero: self.marcar_numero(x))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.botoes.append((numero, btn))
        
        # Frame para controles
        frame_controles = tk.Frame(self.frame_principal, bg='#f0f0f0')
        frame_controles.pack(pady=20)
        
        # Botão para sortear número
        self.btn_sortear = tk.Button(frame_controles, text="Sortear Número", 
                                   command=self.sortear_numero,
                                   font=('Arial', 12), bg='#4CAF50', fg='white')
        self.btn_sortear.pack(side=tk.LEFT, padx=5)
        
        # Botão para nova cartela
        self.btn_nova_cartela = tk.Button(frame_controles, text="Nova Cartela", 
                                        command=self.nova_cartela,
                                        font=('Arial', 12), bg='#2196F3', fg='white')
        self.btn_nova_cartela.pack(side=tk.LEFT, padx=5)
        
        # Label para mostrar número sorteado
        self.label_sorteado = tk.Label(self.frame_principal, text="", 
                                     font=('Arial', 16), bg='#f0f0f0')
        self.label_sorteado.pack(pady=10)
        
        # Label para mostrar números já sorteados
        self.label_historico = tk.Label(self.frame_principal, text="Números sorteados:", 
                                      font=('Arial', 12), bg='#f0f0f0')
        self.label_historico.pack(pady=5)
        
        # Label para mostrar prêmios ganhos
        self.label_premios = tk.Label(self.frame_principal, text="Prêmios ganhos: Nenhum", 
                                    font=('Arial', 12), bg='#f0f0f0', fg='#2196F3')
        self.label_premios.pack(pady=5)
    
    def mostrar_mensagem(self, titulo, mensagem):
        # Criar uma nova janela para a mensagem
        msg_window = tk.Toplevel(self.root)
        msg_window.title(titulo)
        msg_window.geometry("300x100")
        msg_window.transient(self.root)
        
        # Adicionar a mensagem
        label = tk.Label(msg_window, text=mensagem, wraplength=250, pady=20)
        label.pack()
        
        # Fechar automaticamente após 1.5 segundos
        self.root.after(1500, msg_window.destroy)
    
    def sortear_numero(self):
        if len(self.numeros_sorteados) >= 75:
            self.mostrar_mensagem("Fim do Jogo", "Todos os números já foram sorteados!")
            return
            
        numeros_restantes = [n for n in range(1, 76) if n not in self.numeros_sorteados]
        numero_sorteado = random.choice(numeros_restantes)
        self.numeros_sorteados.append(numero_sorteado)
        
        # Atualizar label com número sorteado
        self.label_sorteado.config(text=f"Número sorteado: {numero_sorteado}")
        
        # Atualizar histórico
        historico_text = "Números sorteados: " + ", ".join(map(str, self.numeros_sorteados[-5:]))
        self.label_historico.config(text=historico_text)
        
        # Verificar se número está na cartela
        for num, btn in self.botoes:
            if num == numero_sorteado:
                btn.config(bg='#FF9800')  # Laranja para números marcados
                
        # Verificar se completou a cartela
        self.verificar_vitoria()
        
    def marcar_numero(self, numero):
        if numero in self.numeros_sorteados:
            for num, btn in self.botoes:
                if num == numero:
                    btn.config(bg='#FF9800')  # Laranja para números marcados
                    
    def verificar_vitoria(self):
        # Converter números sorteados em um conjunto para busca mais rápida
        numeros_sorteados_set = set(self.numeros_sorteados)
        
        # Verificar linhas
        for i in range(4):
            linha = self.cartela_matrix[i]
            if all(num in numeros_sorteados_set for num in linha) and "linha" not in self.premios_ganhos:
                self.premios_ganhos.append("linha")
                self.atualizar_premios()
        
        # Verificar colunas
        for j in range(4):
            coluna = [self.cartela_matrix[i][j] for i in range(4)]
            if all(num in numeros_sorteados_set for num in coluna) and "coluna" not in self.premios_ganhos:
                self.premios_ganhos.append("coluna")
                self.atualizar_premios()
        
        # Verificar diagonal principal
        diagonal = [self.cartela_matrix[i][i] for i in range(4)]
        if all(num in numeros_sorteados_set for num in diagonal) and "diagonal" not in self.premios_ganhos:
            self.premios_ganhos.append("diagonal")
            self.atualizar_premios()
        
        # Verificar cartela completa
        if all(num in numeros_sorteados_set for num in self.cartela):
            messagebox.showinfo("BINGO!", "Parabéns! Você completou toda a cartela! ")
            self.root.after(1000, self.nova_cartela)
            
    def atualizar_premios(self):
        if not self.premios_ganhos:
            self.label_premios.config(text="Prêmios ganhos: Nenhum")
        else:
            premios_texto = "Prêmios ganhos: " + ", ".join(self.premios_ganhos)
            self.label_premios.config(text=premios_texto)
            
    def nova_cartela(self):
        # Limpar números sorteados
        self.numeros_sorteados = []
        
        # Gerar nova cartela
        self.criar_cartela()
        
        # Atualizar interface
        for i, (num, btn) in enumerate(self.botoes):
            novo_numero = self.cartela[i]
            btn.config(text=str(novo_numero), bg='SystemButtonFace')
            self.botoes[i] = (novo_numero, btn)
            
        # Limpar labels
        self.label_sorteado.config(text="")
        self.label_historico.config(text="Números sorteados:")
        
        # Limpar prêmios ganhos
        self.premios_ganhos = []
        self.atualizar_premios()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = BingoGame(root)
    root.mainloop()
