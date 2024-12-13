# Importing the tkinter library which is used for creating GUI applications
import tkinter as tk
# Importing ttk module from tkinter for themed widgets
from tkinter import ttk

# Creating the main application window
root = tk.Tk()
# Setting the title of the window
root.title("Widgets Avançados ")
# Setting the size of the window
root.geometry("800x400")
# Setting the background color of the window
root.configure(bg="lightgray")

# Function to display the selected item from the listbox
def exibir_selecao():
    # Getting the selected item from the listbox
    selecionado = listbox.get(listbox.curselection())
    # Updating the result label with the selected item
    label_resultado.config(text=f"Você selecionou: {selecionado}")

def exibir_opcoes():
	linguagem = var_radio.get()
	preferencias = []
	if var_check1.get():
		preferencias.append("Dark Mode")
	if var_check2.get():
		preferencias.append("Auto Save")

	label_opcoes.config(text=f"Linguagem: {linguagem}\nPreferências: {', '.join(preferencias)}")



# Creating a label widget with the text "Selecione um item da Lista"
# Setting the font to Arial, size 24, and background color to light gray
label_titulo = tk.Label(root, text="Selecione um item da Lista", font=("Arial", 24), bg="lightgray")
# Placing the label in the window with some padding
label_titulo.pack(pady=10)

# Creating a frame to hold the listbox and its scrollbar
frame_listbox = tk.Frame(root)
# Placing the frame in the window with some padding
frame_listbox.pack(pady=10)

# Creating a scrollbar widget and associating it with the frame
scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)
# Creating a listbox widget and associating it with the frame
listbox = tk.Listbox(frame_listbox, height=4, yscrollcommand=scrollbar.set, font=("Arial", 20), bg="white", fg="black", selectbackground="green", selectforeground="white", activestyle="dotbox")

# Configuring the scrollbar to work with the listbox
scrollbar.config(command=listbox.yview)
# Placing the scrollbar on the right side and making it fill the Y-axis
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Placing the listbox on the left side and making it fill both X and Y axes
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Defining a dictionary with programming languages as keys and their emojis as values
# The commented line shows an alternative list of items without emojis
itens = {"Python": "", "Java": "", "C++": "", "Ruby": "", "JavaScript": "", "Go": "", "Swift": "", "Kotlin": ""}
#itens = ["Python", "Java", "C++", "Ruby", "JavaScript", "Go", "Swift", "Kotlin"]

# Iterating over the dictionary items (language and emoji)
for item, emoji in itens.items():
    # Inserting each language and its emoji into the listbox
    listbox.insert(tk.END, f"{item} {emoji}")

# Creating a button widget labeled "Exibir Seleção"
# Setting the font to Arial, size 18, background color to green, and text color to white
# Associating the button with the exibir_selecao function to display the selected item
botao_exibir = tk.Button(root, text="Exibir Seleção", font=("Arial", 18), bg="green", fg="white", command=exibir_selecao)
# Placing the button in the window with some padding
botao_exibir.pack(pady=10)

# Creating a label widget to display the result of the selection
# Setting the font to Arial, size 12, and background color to light gray
label_resultado = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
# Placing the result label in the window with some padding
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



# Starting the Tkinter event loop to run the application
root.mainloop()