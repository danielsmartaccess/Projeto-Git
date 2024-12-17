# **Jogo da Adivinhação com Tkinter**

"""
Este jogo utiliza os conceitos abordados até agora no curso, incluindo:
- Widgets do Tkinter (Labels, Buttons, Entry, Frames).
- Manipulação de eventos (command, bind).
- Funções e variáveis.
- Estruturas de controle (if/else).

**Objetivo do Jogo:**
O jogador deve adivinhar um número secreto entre 1 e 100. A interface exibirá dicas como "muito alto" ou "muito baixo" até o jogador acertar.

"""

# Importando a biblioteca Tkinter
import tkinter as tk
import random

# **Função para iniciar o jogo e definir o número secreto**
def iniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = random.randint(1, 100)  # Número aleatório entre 1 e 100
    tentativas = 0  # Contador de tentativas
    label_mensagem.config(text="Tente adivinhar o número entre 1 e 100!", fg="black")
    entry_tentativa.delete(0, tk.END)  # Limpar o campo de entrada
    label_tentativas.config(text="Tentativas: 0")

# **Função para verificar a tentativa do jogador**
def verificar_tentativa():
    global tentativas
    try:
        tentativa = int(entry_tentativa.get())  # Captura o valor digitado
        tentativas += 1  # Incrementa o número de tentativas
        label_tentativas.config(text=f"Tentativas: {tentativas}")
        
        # Verifica se a tentativa está correta
        if tentativa == numero_secreto:
            label_mensagem.config(text=f"Parabéns! Você acertou em {tentativas} tentativas! 🎉", fg="green")
        elif tentativa < numero_secreto:
            label_mensagem.config(text="Muito baixo! Tente um número maior.", fg="blue")
        else:
            label_mensagem.config(text="Muito alto! Tente um número menor.", fg="orange")
    except ValueError:
        label_mensagem.config(text="Por favor, insira apenas números!", fg="red")
        entry_tentativa.delete(0, tk.END)

# **Função para encerrar o jogo**
def encerrar_jogo():
    root.destroy()  # Fecha a janela

# **Janela Principal**
root = tk.Tk()
root.title("Jogo da Adivinhação 🎲")
root.geometry("400x300")
root.configure(bg="lightyellow")

# **Widgets da Interface**
# Título do jogo
label_titulo = tk.Label(root, text="Jogo da Adivinhação", font=("Arial", 18, "bold"), bg="lightyellow")
label_titulo.pack(pady=10)

# Mensagem inicial
label_mensagem = tk.Label(root, text="Tente adivinhar o número entre 1 e 100!", font=("Arial", 12), bg="lightyellow")
label_mensagem.pack(pady=10)

# Campo de entrada para a tentativa do jogador
entry_tentativa = tk.Entry(root, font=("Arial", 14), justify="center")
entry_tentativa.pack(pady=5)

# Botão para verificar a tentativa
botao_verificar = tk.Button(root, text="Verificar", font=("Arial", 12), bg="green", fg="white", command=verificar_tentativa)
botao_verificar.pack(pady=5)

# Botão para reiniciar o jogo
botao_reiniciar = tk.Button(root, text="Reiniciar", font=("Arial", 12), bg="blue", fg="white", command=iniciar_jogo)
botao_reiniciar.pack(pady=5)

# Botão para encerrar o jogo
botao_encerrar = tk.Button(root, text="Sair", font=("Arial", 12), bg="red", fg="white", command=encerrar_jogo)
botao_encerrar.pack(pady=5)

# Label para mostrar o número de tentativas
label_tentativas = tk.Label(root, text="Tentativas: 0", font=("Arial", 12), bg="lightyellow")
label_tentativas.pack(pady=5)

# Iniciar o jogo definindo o número secreto
iniciar_jogo()

# Executando o loop principal da interface
tk.mainloop()

"""
### **Explicação do Funcionamento do Jogo**

1. **Widgets Utilizados:**
   - **Label:** Para mostrar mensagens e feedback ao usuário.
   - **Entry:** Permite que o usuário digite sua tentativa.
   - **Button:** Executa ações como verificar a tentativa, reiniciar ou sair do jogo.

2. **Funções Principais:**
   - `iniciar_jogo()`: Gera um número aleatório e reinicia as configurações iniciais.
   - `verificar_tentativa()`: Captura o valor digitado pelo usuário, compara com o número secreto e exibe mensagens de feedback (muito alto, muito baixo ou correto).
   - `encerrar_jogo()`: Fecha a aplicação.

3. **Estruturas de Controle:**
   - **if/else**: Verifica a condição da tentativa e fornece o feedback adequado.
   - **try/except**: Garante que apenas valores numéricos sejam aceitos, evitando erros de entrada.

4. **Interatividade:**
   - O botão "Verificar" processa a tentativa.
   - O botão "Reiniciar" começa um novo jogo.
   - O botão "Sair" fecha a aplicação.

### **Conclusão:**
Este jogo demonstra a aplicação prática dos conceitos vistos até agora, como widgets, funções, tratamento de eventos e estruturas de controle. O aluno pode expandir o jogo, como adicionar um cronômetro ou salvar os resultados em um arquivo. 🚀
"""
