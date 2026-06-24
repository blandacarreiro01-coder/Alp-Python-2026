usuarios = []


def cadastrar():
    print("\n--- CADASTRO ---")
    usuario = input("Escolha um login: ").strip()

    for u in usuarios:
        if u["login"] == usuario:
            print("Login já cadastrado!")
            return

    senha = input("Escolha uma senha: ").strip()
    usuarios.append({"login": usuario, "senha": senha})
    print(f"Usuário '{usuario}' cadastrado com sucesso!")
    print("Usuários cadastrados:", usuarios)

def fazer_login():
    print("\n--- LOGIN ---")
    usuario = input("Login: ").strip()
    senha = input("Senha: ").strip()

    for u in usuarios:
        if u["login"] == usuario:
            if u["senha"] == senha:
                print(f"Bem-vindo(a), {usuario}! Acesso liberado.")
            else:
                print("Senha incorreta. Acesso negado.")
            return

    print("Usuário não encontrado. Acesso negado.")

while True:
    print("\n=== SISTEMA DE LOGIN (Lista de Dicionários) ===")
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