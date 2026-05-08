valor =float(input("Digite o valor da compra: " ))
print("-" *50)
print("""[1] A vista(em especie): 15%
[2] Cartão de debito: 10% 
[3] Cartão de credito: 5%""")
opcao =int(input("Escolha uma opção:  "))
print("-" *50)
if opcao == 1:
    desconto = valor * (15/100)
    preco_final = valor - desconto
    print(f"O valor a ser pago é igual a: {preco_final}")
if opcao == 2:
    desconto = valor * (10/100)
    preco_final = valor - desconto
    print(f"O valor a ser pago é igual a: {preco_final}")
if opcao == 3:
    desconto = valor * (5/100)
    preco_final = valor - desconto
    print(f"O valor a ser pago é igual a: {preco_final}")
else:
    print("Opção invalida,por favor escolha uma disponivel.")