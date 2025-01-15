import tkinter as tk

root = tk.Tk()
root.title("Eventos e Interatividade 🎯")
root.geometry("400x300")
root.configure(bg="lightgray")

def ao_clicar():
	print("Botão foi clicado! 🚀")

def ao_pressionar_tecla(event):
    print(f"Você pressionou: {event.char} 🆘")

def ao_mover_mouse(event):
	print(f"Mouse em: x={event.x}, y={event.y}")

botao = tk.Button(root, text="Clique Aqui!", font=("Arial", 14), bg="green", fg="white", command=ao_clicar)
botao.pack(pady=20)

root.bind("<Key>", ao_pressionar_tecla)

root.bind("<Motion>", ao_mover_mouse)

root.mainloop()
