while True:
    try:
        nome = input("Digite seu nome: ").strip()
        senha = input("Digite sua senha: ").strip()
        if nome.lower() != senha.lower():
            print("Usuário cadastrado com sucesso.")
            break
        else:
            print("Nome de usuário e senha não podem ser iguais.")
    except ValueError:
        print("Entrada inválida. Por favor, tente novamente.")