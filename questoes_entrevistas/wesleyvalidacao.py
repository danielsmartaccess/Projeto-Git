def cadastro():
    nome = input('Digite seu nome: tem que ter mais de 3 caracteres:')
    idade = int(input('Digite sua idade: entre 0 e 150:'))
    salario = float(input('Digite seu salário: maior que zero:'))
    sexo = input('Digite seu sexo: M ou F:').upper()
    estado_civil = input('Digite seu estado civil: S, C, V, D:').upper()

    while True:
        if len(nome) <=3 or idade < 0 or idade > 150 or salario <= 0 or sexo != 'M' and sexo != 'F' or estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
            print('Dados inválidos. Digite novamente.')
            return cadastro()
        else:
            print('Cadastro realizado com sucesso!')
            break
cadastro()