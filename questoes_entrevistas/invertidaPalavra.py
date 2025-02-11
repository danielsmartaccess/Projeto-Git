# Solução

def inverter_string(texto):
    """
    Inverte os caracteres de uma string fornecida.

    Args:
        texto (str): A string que será invertida.

    Returns:
        str: A string invertida.

    Example:
        >>> inverter_string("Python")
        'nohtyP'
    """
    # O slice [::-1] funciona da seguinte forma:
    # [início:fim:passo]
    # : - significa que queremos todos os caracteres (do início ao fim)
    # -1 - é o passo negativo, que faz a leitura da direita para esquerda
    # Exemplo: "Python" -> "nohtyP"
    return texto[::-1]

# Exemplos de diferentes formas de slice
def exemplos_slice():
    texto = "Python"
    
    # [::1] - normal, da esquerda para direita (passo 1)
    print(texto[::1])   # Saída: Python
    
    # [::2] - pula 1 caractere
    print(texto[::2])   # Saída: Pto
    
    # [::-2] - invertido, pulando 1 caractere
    print(texto[::-2])  # Saída: nhy
    
    # [1:4] - do índice 1 até o 3 (4-1)
    print(texto[1:4])   # Saída: yth
    
    # [4:1:-1] - do índice 4 até o 2, invertido
    print(texto[4:1:-1])  # Saída: oht

# Teste dos exemplos
exemplos_slice()

print(inverter_string("Python"))  # Saída esperada: nohtyP