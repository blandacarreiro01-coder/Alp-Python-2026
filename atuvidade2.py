#2. Construa um programa que solicite ao usuário dois números positivos. Em seguida, o programa deve apresentar o seguinte
#menu:
#1. Média ponderada, com pesos 2 e 3, respectivamente
#2. Quadrado da soma dos 2 números
#3. Cubo do menor número
#Escolha uma opção:
#De acordo com a opção informada, o programa deve calcular a operação apresentada no menu. Se a opção escolhida for inválida, o programa deve mostrar a mensagem “Opção inválida” e ser encerrado.#

num1 = int(input("Escreva o primeiro numero: "))
num2 = int(input("Escreva o segundo numero: "))
print(""" menu:
1. Media ponderada, com peso 2 e 3, respectivamente
2.Quadrado da soma de dos 2 números
3. Cubo do menor numero""")
opcao_escolhida = int(input("Escolha uma opção :"))
if opcao_escolhida== 1 :
    resultado = ((num1* 2) + (num2*3))/5
    print(f"O resultado é igual a: {resultado}")
elif opcao_escolhida== 2:
   resultado = (num1+num2)**2
   print(f"O resultado é igual a: {resultado}")
elif opcao_escolhida == 3:
    if num1 > num2:
     resultado = num1**2
    else:
     resultado = num2**3
    print(f"O resultado é igual a:{resultado} ")
else:
 print("Opção invalida, por favor escolha uma disponivel.")
