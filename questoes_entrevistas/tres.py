def segundo_maior(lista):
    lista = list(set(lista))  # Removendo duplicatas
    lista.sort()  # Ordenando em ordem decrescente
    return lista[-2] if len(lista) > 1 else None

print(segundo_maior([10, 20, 4, 45, 99, 99]))  # Saída esperada: 45