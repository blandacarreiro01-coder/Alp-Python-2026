"""4. Imagine um sistema de caixa eletrônico. Construa um programa que receba a senha de um correntista para validar o seu acesso ao sistema. Considere que a senha fictícia do correntista é 123456. Considere as seguintes restrições:
• quando a senha estiver correta, mostrar a mensagem: “Olá, <SEUNOME>. Seja bem-vindo ao nosso banco!"
• quando o usuário errar a senha pela primeira vez, mostrar a mensagem: “Senha incorreta! Você ainda tem 2 tentativas.”
• se o usuário errar a senha pela segunda vez, mostrar a mensagem: “Senha incorreta! Você ainda tem 1 tentativa.”
• se o usuário errar a senha novamente, mostrar a mensagem “Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.” e o programa deve ser encerrado."""
nome = input("Digite o seu nome: ")
senha_correta = 123456
tentativas = 3 
while tentativas > 0: 
    senha = int(input("Digite sua senha:"))
    if senha == senha_correta: 
        print(f"Olá! bem-vindo(a) {nome} ao nosso banco!")
        break
    else: 
        tentativas -= 1 
        if tentativas == 2:
            print("Senha incorreta! você ainda tem 2 tentativas.")
        elif tentativas == 1:
            print("Senha incorreta! você ainda tem 1 tentativa.")
        else: 
            print("Sua senha foi bloqueada, Por favor dirija-se a um dos nossos caixas.")
            