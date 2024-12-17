from cProfile import label
import tkinter as tk

root = tk.Tk()
root.title("Layout Tkinter")
root.geometry("400x300")
root.configure(bg="lightblue")




label1 = tk.Label(root, text="Label 1 (TOP)", font=("Arial", 14), bg="red", fg="white" )
label1.pack(pady=10, fill=tk.X)
label4 = tk.Label(root, text="Label 4 (BOTTOM)", font=("Arial", 14), bg="yellow", fg="black")
label4.pack(side=tk.BOTTOM, pady=10, fill=tk.X)
label2 = tk.Label(root, text="Labe 2 (LEFT)", font=("Arial",14), bg="green", fg="white")
label2.pack(side=tk.LEFT, padx=10, fill=tk.Y)

label3 = tk.Label(root, text="Label 3 (RIGHT)", font=("Arial", 14), bg="blue", fg="white")
label3.pack(side=tk.RIGHT, padx=10, fill=tk.Y)


botao = tk.Button(root, text="Fechar", font=("Arial", 14), bg="orange", fg="white", command=root.destroy)

botao.pack(pady=10, fill=tk.X)


root.mainloop()
