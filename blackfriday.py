"""2. Refaça a questão 9 da Black Friday (código em anexo) adicionando estrutura de repetição. O programa deve parar quando a opção zero for informada."""
while True:
    valor = float(input("Digite o valor da compra: "))
    print('-' * 50)
    opcao = int(input(f"""[1] A vista 15% de desconto 
[2] Cartão de debito 10% de desconto
[3] Cartão de credito 5% de desconto
[0] Sair
Selecione a opçao desejada: """))
    print('-' * 50)
    if opcao == 0:
        print("Programa encerrado.")
        break
    if opcao == 1:
        print(f"O valor do desconto é de R${valor * 0.15:.2f} e o valor final a ser pago é de R${valor * 0.85:.2f}")
    elif opcao ==2:
        print(f"O valor do desconto é de R${valor * 0.10:.2f} e o valor final a ser pago é de R${valor * 0.90:.2f}")
    elif opcao ==3:
        print(f"O valor do desconto é de R${valor * 0.05:.2f} e o valor final a ser pago é de R${valor * 0.95:.2f}")
    else: 
        print("Opção inválida!")
