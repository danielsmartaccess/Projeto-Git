def validar_nome(nome):
    return len(nome) > 3

def validar_idade(idade):
    return 0 <= idade <= 150

def validar_salario(salario):
    return salario > 0

def validar_sexo(sexo):
    return sexo.upper() in ['M', 'F']

def validar_estado_civil(estado):
    return estado.upper() in ['S', 'C', 'V', 'D']

def main():
    # Validação do nome
    while True:
        nome = input("Digite o nome (mais que 3 caracteres): ")
        if validar_nome(nome):
            break
        print("Nome inválido! Deve ter mais que 3 caracteres.")

    # Validação da idade
    while True:
        try:
            idade = int(input("Digite a idade (entre 0 e 150): "))
            if validar_idade(idade):
                break
            print("Idade inválida! Deve estar entre 0 e 150.")
        except ValueError:
            print("Por favor, digite um número válido.")

    # Validação do salário
    while True:
        try:
            salario = float(input("Digite o salário (maior que zero): "))
            if validar_salario(salario):
                break
            print("Salário inválido! Deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um número válido.")

    # Validação do sexo
    while True:
        sexo = input("Digite o sexo (M/F): ")
        if validar_sexo(sexo):
            break
        print("Sexo inválido! Digite M ou F.")

    # Validação do estado civil
    while True:
        estado_civil = input("Digite o estado civil (S/C/V/D): ")
        if validar_estado_civil(estado_civil):
            break
        print("Estado civil inválido! Digite S, C, V ou D.")

    print("\nInformações validadas com sucesso!")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Sexo: {sexo.upper()}")
    print(f"Estado Civil: {estado_civil.upper()}")

if __name__ == "__main__":
    main()
