# Solução

# Primeira implementação: Retorna uma lista com n números da sequência
def fibonacci(n):
    # Inicializa a sequência com os dois primeiros números
    sequencia = [0, 1]
    
    # Gera os próximos números da sequência até atingir n números
    for _ in range(n - 2):
        sequencia.append(sequencia[-1] + sequencia[-2])  # Cada novo número é a soma dos dois anteriores
    
    return sequencia[:n]  # Retorna os n primeiros números da sequência

# Entrada do usuário e exibição do resultado da primeira implementação
n = int(input('Quantos números de Fibonacci você deseja? '))
print(fibonacci(n))


# Segunda implementação: Imprime os números um por um
def fibonaccii():
    # Obtém a quantidade de números desejada
    n = int(input("Digite um número: "))
    
    # Inicializa os dois primeiros números
    a = 0  # Primeiro número
    b = 1  # Segundo número
    
    # Loop para gerar e imprimir n números
    for i in range(n):
        print(a)  # Imprime o número atual
        a, b = b, a + b  # Atualiza os valores usando atribuição múltipla
        
fibonaccii()

def fibonacci(n):
    sequencia = [0, 1]
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    for i in range(2, n):
        numero = sequencia[-1] + sequencia[-2]
        sequencia.append(numero)
        
    return print(sequencia)

fibonacci(9)