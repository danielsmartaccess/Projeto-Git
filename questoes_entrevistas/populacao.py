# Coleta dados iniciais
pop_a = int(input('Digite a população do país A: '))
pop_b = int(input('Digite a população do país B: '))

# Coleta taxas de crescimento e converte para decimal
taxa_a = float(input('Digite a taxa de crescimento anual da população do país A (em %): ')) 
taxa_b = float(input('Digite a taxa de crescimento anual da população do país B (em %): '))

# Inicializa contador de anos
anos = 0

# Lógica principal:
# Se população A é menor que B, calcula quanto tempo levará para ultrapassar
if pop_a < pop_b:
    while pop_a < pop_b:
        pop_a = pop_a + ((pop_a * taxa_a)/100)  # Crescimento do país A
        pop_b = pop_b + ((pop_b * taxa_b)/ 100)  # Crescimento do país B
        anos += 1
    print(f"Serão necessários {anos} ano(s) para a população do país A igualar ou ultrapassar a população do país B.")
else:
    print("A população do país A já é maior que a população do país B!")

# Exibe resultados finais
print(f"População final do país A: {(pop_a)} habitantes")
print(f"População final do país B: {(pop_b)} habitantes")