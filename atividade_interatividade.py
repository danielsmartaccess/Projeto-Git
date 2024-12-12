import tkinter as tk

root = tk.Tk()
root.title("Interatividade em Tkinter 🖱️")
root.geometry("400x300")
root.configure(bg="lightyellow")

def atualizar_label(event):
	label_resultado.config(text=f"Tecla pressionada: {event.char}")

def botao_clicado():
	print("Botão clicado! 🎉")

root.bind("<Key>", atualizar_label)

label_instrucao = tk.Label(root, text="Pressione uma tecla ou clique no botão!", font=("Arial", 14), bg="lightyellow")
label_instrucao.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 14), bg="lightyellow")
label_resultado.pack(pady=10)

botao_interativo = tk.Button(root, text="Clique Aqui", font=("Arial", 14), bg="blue", fg="white", command=botao_clicado)
botao_interativo.pack(pady=10)

root.bind("<Key>", atualizar_label)

root.mainloop()