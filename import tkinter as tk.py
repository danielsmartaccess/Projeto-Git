import tkinter as tk

root = tk.Tk()
root.title("Interface de Idade ")
root.geometry("400x300")
root.configure(bg="#FFE4E1")

def exibir_idade():
    idade = entrada.get()
    print(f"Idade digitada: {idade} anos")

def limpar_texto():
    entrada.delete(0, tk.END)

label = tk.Label(root, text="Digite sua idade:", font=("Verdana", 14, "bold"), bg="#FFE4E1", fg="#8B4513")
label.pack(pady=20)

entrada = tk.Entry(
    root,
    font=("Verdana", 12),
    width=10,
    justify="center",
    bg="white",
    fg="#4A4A4A"
)
entrada.pack(pady=15)

frame_botoes = tk.Frame(root, bg="#FFE4E1")
frame_botoes.pack(pady=20)

botao_exibir = tk.Button(
    frame_botoes,
    text="Exibir",
    font=("Verdana", 12),
    bg="#20B2AA",
    fg="white",
    width=8,
    command=exibir_idade,
    cursor="hand2"
)
botao_exibir.pack(side=tk.LEFT, padx=10)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    font=("Verdana", 12),
    bg="#FF69B4",  
    fg="white",
    width=8,
    command=limpar_texto,
    cursor="hand2"
)
botao_limpar.pack(side=tk.LEFT, padx=10)

root.mainloop()
