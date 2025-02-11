
def digite_valor():
    while True:
        nota = int(input("Digite um valor entre 0 e 10: "))
        if 0 <= nota <= 10:
            print("Valor válido.")
            break
        else:
            print(f"O valor digitado foi: {nota}, Digite um valor entre 0 e 10")
        

digite_valor()

    

