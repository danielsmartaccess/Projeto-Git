import tkinter as tk

def somar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos!")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Simples 📏")
root.geometry("800x600")
root.configure(bg="lightblue")

# Adicionando um rótulo de título
label_titulo = tk.Label(root, text="Calculadora Simples", font=("Arial Bold", 16), bg="lightyellow")
label_titulo.pack(pady=10)

# Adicionando campos de entrada
entrada1 = tk.Entry(root, font=("Arial", 14))
entrada1.pack(pady=5)
entrada2 = tk.Entry(root, font=("Arial", 14))
entrada2.pack(pady=5)

# Botão para calcular a soma
botao_somar = tk.Button(root, text="Somar", font=("Arial", 14), bg="blue", fg="white", command=somar)
botao_somar.pack(pady=10)

# Rótulo para exibir o resultado
label_resultado = tk.Label(root, text=None, font=("Arial", 14), bg="lightblue")
label_resultado.pack(pady=10)

# Loop principal
root.mainloop()
