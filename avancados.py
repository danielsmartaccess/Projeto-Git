# Importando a biblioteca tkinter que é usada para criar aplicativos GUI
import tkinter as tk
# Importando o módulo ttk do tkinter para widgets temáticos
from tkinter import ttk

# Criando a janela principal do aplicativo
root = tk.Tk()
# Definindo o título da janela
root.title("Widgets Avançados ")
# Definindo o tamanho da janela
root.geometry("800x400")
# Definindo a cor de fundo da janela
root.configure(bg="lightgray")

# Função para exibir o item selecionado da listbox
def exibir_selecao():
    # Obtendo o item selecionado da listbox
    selecionado = listbox.get(listbox.curselection())
    # Atualizando o rótulo de resultado com o item selecionado
    label_resultado.config(text=f"Você selecionou: {selecionado}")

def exibir_opcoes():
    linguagem = var_radio.get()
    preferencias = []
    if var_check1.get():
        preferencias.append("Dark Mode")
    if var_check2.get():
        preferencias.append("Auto Save")

    # Atualizando o rótulo de opções com a linguagem e preferências selecionadas
    label_opcoes.config(text=f"Linguagem: {linguagem}\nPreferências: {', '.join(preferencias)}")

# Criando um widget de rótulo com o texto "Selecione um item da Lista"
# Definindo a fonte para Arial, tamanho 24, e cor de fundo para cinza claro
label_titulo = tk.Label(root, text="Selecione um item da Lista", font=("Arial", 24), bg="lightgray")
# Colocando o rótulo na janela com algum espaçamento
label_titulo.pack(pady=10)

# Criando um frame para conter a listbox e sua barra de rolagem
frame_listbox = tk.Frame(root)
# Colocando o frame na janela com algum espaçamento
frame_listbox.pack(pady=10)

# Criando um widget de barra de rolagem e associando-o ao frame
scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)
# Criando um widget de listbox e associando-o ao frame
listbox = tk.Listbox(frame_listbox, height=4, yscrollcommand=scrollbar.set, font=("Arial", 20), bg="white", fg="black", selectbackground="green", selectforeground="white", activestyle="dotbox")

# Configurando a barra de rolagem para funcionar com a listbox
scrollbar.config(command=listbox.yview)
# Colocando a barra de rolagem no lado direito e fazendo-a preencher o eixo Y
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Colocando a listbox no lado esquerdo e fazendo-a preencher os eixos X e Y
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Definindo um dicionário com linguagens de programação como chaves e seus emojis como valores
# A linha comentada mostra uma lista alternativa de itens sem emojis
itens = {"Python": "", "Java": "", "C++": "", "Ruby": "", "JavaScript": "", "Go": "", "Swift": "", "Kotlin": ""}
#itens = ["Python", "Java", "C++", "Ruby", "JavaScript", "Go", "Swift", "Kotlin"]

# Iterando sobre os itens do dicionário (linguagem e emoji)
for item, emoji in itens.items():
    # Inserindo cada linguagem e seu emoji na listbox
    listbox.insert(tk.END, f"{item} {emoji}")

# Criando um widget de botão rotulado "Exibir Seleção"
# Definindo a fonte para Arial, tamanho 18, cor de fundo para verde, e cor do texto para branco
# Associando o botão à função exibir_selecao para exibir o item selecionado
botao_exibir = tk.Button(root, text="Exibir Seleção", font=("Arial", 18), bg="green", fg="white", command=exibir_selecao)
# Colocando o botão na janela com algum espaçamento
botao_exibir.pack(pady=10)

# Criando um widget de rótulo para exibir o resultado da seleção
# Definindo a fonte para Arial, tamanho 12, e cor de fundo para cinza claro
label_resultado = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
# Colocando o rótulo de resultado na janela com algum espaçamento
label_resultado.pack(pady=10)

var_radio = tk.StringVar(value="Python")
label_radio = tk.Label(root, text="Escolha sua linguagem favorita:", font=("Arial", 18), bg="lightgray")
label_radio.pack(pady=10)

for linguagem in ["Python", "Java", "C++"]:
    rb = tk.Radiobutton(root, text=linguagem, variable=var_radio, value=linguagem, bg="lightgray")
    rb.pack(anchor=tk.CENTER)

var_check1 = tk.BooleanVar()
var_check2 = tk.BooleanVar()

check1 = tk.Checkbutton(root, text="Dark Mode", variable=var_check1, bg="lightgray")
check2 = tk.Checkbutton(root, text="Auto Save", variable=var_check2, bg="lightgray")
check1.pack(anchor=tk.CENTER)
check2.pack(anchor=tk.CENTER)

botao_opcoes = tk.Button(root, text="Exibir Opções", font=("Arial", 12), bg="blue", fg="white", command=exibir_opcoes)
botao_opcoes.pack(pady=10, padx=10, anchor=tk.CENTER)

label_opcoes = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
label_opcoes.pack(pady='10', padx=10, anchor=tk.CENTER)

# Iniciando o loop de eventos do Tkinter para executar o aplicativo
root.mainloop()