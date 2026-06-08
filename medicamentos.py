"""3. Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o usuário informou cinco medicamentos distintos). O programa deve informar o nome e o preço do medicamento mais barato, bem como a média aritmética dos preços informados."""

menor_nome = ""
menor_preco = 0
soma = 0 
for contador in range(1,6):
    print(f"------Medicamento {contador}------")
    nome = input("Nome: ")
    preco = float(input("Preço: R$ "))

    soma += preco

    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        menor_nome = nome

media = soma / 5 
print("========= RESULTADO =========")
print(f"Medicamento mais barato: {menor_nome}")
print(f"Preço: R$ {menor_preco:.2f}")
print(f"Média dos preços: R$ {media:.2f}")