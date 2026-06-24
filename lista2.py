# Questão 2 - Cadastro e Login com Duas Listas

logins = []
senhas = []

def cadastrar():
    print("\n--- CADASTRO ---")
    usuario = input("Escolha um login: ").strip()
    if usuario in logins:
        print("Login já cadastrado!")
        return
    senha = input("Escolha uma senha: ").strip()
    logins.append(usuario)
    senhas.append(senha)
    print(f"Usuário '{usuario}' cadastrado com sucesso!")
    print("Logins cadastrados:", logins)

def fazer_login():
    print("\n--- LOGIN ---")
    usuario = input("Login: ").strip()
    senha = input("Senha: ").strip()

    if usuario in logins:
        indice = logins.index(usuario)
        if senhas[indice] == senha:
            print(f"Bem-vindo(a), {usuario}! Acesso liberado.")
        else:
            print("Senha incorreta. Acesso negado.")
    else:
        print("Usuário não encontrado. Acesso negado.")

while True:
    print("\n=== SISTEMA DE LOGIN (Listas) ===")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        fazer_login()
    elif opcao == "3":
        print("Encerrando.")
        break
    else:
        print("Opção inválida.")