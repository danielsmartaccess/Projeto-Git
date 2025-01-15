# **Jogo de Cassino: Máquina de Puxar Alavanca em Tkinter**

"""
Objetivo: Criar um jogo de cassino com interface gráfica usando Tkinter. 
O jogador "puxa a alavanca" e três figuras aleatórias aparecem. 
Se as três figuras forem iguais, o jogador vence!

Este código usa apenas os conceitos e métodos já vistos em aula.
"""

import tkinter as tk
import random

# Lista de símbolos possíveis para o jogo
simbolos = ["🍒", "🍋", "🔔", "🍉", "⭐", "💎"]

# Função para rodar os slots
def rodar_slots():
    # Escolhendo três símbolos aleatórios
    slot1 = random.choice(simbolos)
    slot2 = random.choice(simbolos)
    slot3 = random.choice(simbolos)

    # Atualizando os Labels com os símbolos sorteados
    label_slot1.config(text=slot1)
    label_slot2.config(text=slot2)
    label_slot3.config(text=slot3)

    # Verificando se o jogador venceu
    if slot1 == slot2 == slot3:
        label_resultado.config(text="🎉 Você venceu! Parabéns! 🎉", fg="green")
    else:
        label_resultado.config(text="Tente novamente! 😢", fg="red")

# Criando a janela principal
root = tk.Tk()
root.title("Máquina de Cassino 🎰")
root.geometry("1200x900")
root.configure(bg="black")

# Título do jogo
label_titulo = tk.Label(root, text="Cassino Python 🎰", font=("Arial", 20), bg="black", fg="white")
label_titulo.pack(pady=10)

# Frame para exibir os slots
frame_slots = tk.Frame(root, bg="black")
frame_slots.pack(pady=20)

# Labels para os slots
label_slot1 = tk.Label(frame_slots, text="?", font=("Arial", 30), bg="white", width=5)
label_slot1.pack(side=tk.LEFT, padx=5)

label_slot2 = tk.Label(frame_slots, text="?", font=("Arial", 30), bg="white", width=5)
label_slot2.pack(side=tk.LEFT, padx=5)

label_slot3 = tk.Label(frame_slots, text="?", font=("Arial", 30), bg="white", width=5)
label_slot3.pack(side=tk.LEFT, padx=5)

# Legenda dos símbolos
label_legenda = tk.Label(root, text="Símbolos possíveis: 🍒, 🍋, 🔔, 🍉, ⭐, 💎", font=("Comic Sans MS", 30), bg="black", fg="white")
label_legenda.pack(pady=5)

# Botão para puxar a alavanca
botao_jogar = tk.Button(root, text="Puxar Alavanca 🎲", font=("Arial", 24), bg="green", fg="white", command=rodar_slots)
botao_jogar.pack(pady=20)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="Boa sorte!", font=("Arial", 32), bg="black", fg="white")
label_resultado.pack(pady=10)

# Loop principal
def iniciar_jogo():
    label_resultado.config(text="Boa sorte!", fg="white")

iniciar_jogo()
root.mainloop()

"""
**Explicação do Código:**
1. **Lista de símbolos:** Define os possíveis símbolos que aparecem nos slots.
2. **Função `rodar_slots()`:** Escolhe três símbolos aleatórios e verifica se o jogador venceu.
3. **Widgets:**
   - Labels: Usados para exibir os símbolos dos slots e o resultado.
   - Botão: Permite ao jogador "puxar a alavanca".
4. **Interatividade:** Atualiza os slots e o resultado ao clicar no botão.
5. **Visual:** Personalizado com cores e fontes para simular o ambiente de um cassino.
""" 
