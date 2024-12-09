# Widgets for the GUI

import tkinter as tk

root = tk.Tk()
root.title("Minha Janela Interativa 🙌")
root.geometry("800x600")
root.configure(bg="white")

label = tk.Label(root, text="Bem-vindo ao Tkinter!", font=("Arial Bold", 26), bg="white", fg="green")
label.pack(pady=80)  # Exibindo o rótulo com espaçamento vertical

entrada = tk.Entry(root, font=("Arial", 14),fg="green")
entrada.pack(pady=10)  # Exibindo a entrada com espaçamento vertical


def exibir_texto():
	texto = entrada.get()  # Obtendo o texto inserido pelo usuário
	print(f"Você digitou: {texto}")

botao_exibir = tk.Button(root, text="Exibir Texto", font=("Arial", 14), bg="blue", fg="white", command=exibir_texto)
botao_exibir.pack(pady=10)

root.mainloop()