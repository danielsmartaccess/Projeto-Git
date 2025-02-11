# Solução

def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

print(eh_palindromo("Ame a ema"))  # Saída esperada: True

def eh_palindromo2(texto):
    texto1 = texto.strip().lower()
    if texto == texto1[::-1]:
        return True
    else:
        return False

 
def eh_palindromo(texto):

    texto = ''.join(texto.lower().split())

    texto = ''.join(c for c in texto if c.isalnum())
    
    return texto == texto[::-1]

palavra = input("Digite uma palavra ou frase: ")


if eh_palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")