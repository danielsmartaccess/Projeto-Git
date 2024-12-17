#Usando o grid para organizar os widgets
import tkinter as tk

def criar_interface_grid():
    janela_grid = tk.Tk()
    janela_grid.title("Layout Grid")
    janela_grid.geometry("400x300")
    janela_grid.configure(bg="lightblue")
    
    tk.Label(janela_grid, text="Row 0, Col 0", bg="red", fg="white").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(janela_grid, text="Row 0, Col 1", bg="green", fg="white").grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(janela_grid, text="Row 1, Col 0", bg="blue", fg="white").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(janela_grid, text="Row 1, Col 1", bg="purple", fg="white").grid(row=1, column=3, padx=5, pady=5)
    
    tk.Button(janela_grid, text="Fechar", command=janela_grid.destroy).grid(row=2, column=1, columnspan=4, padx=5, pady=5)
    
    return janela_grid

if __name__ == "__main__":
    janela = criar_interface_grid()
    janela.mainloop()