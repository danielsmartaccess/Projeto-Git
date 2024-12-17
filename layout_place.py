import tkinter as tk

def criar_interface_place():
    janela_place = tk.Tk()
    janela_place.title("Layout Place")
    janela_place.geometry("400x300")
    janela_place.configure(bg="lightgray")

    # Label usando coordenadas absolutas
    tk.Label(janela_place, text="Posição Absoluta",font=("Arial", 14),   bg="red", fg="white").place(x=50, y=50)

    # Label usando coordenadas relativas
    tk.Label(janela_place, text="Posição Relativa",font=("Arial", 14), bg="blue", fg="white").place(x=50, y=100)

    # Botão de fechar
    tk.Button(janela_place, text="Fechar", command=janela_place.destroy).place(x=100, y=200)

    return janela_place

if __name__ == "__main__":
    janela = criar_interface_place()
    janela.mainloop()