#1. Construa um programa que receba um número inteiro positivo informado pelo usuário. Caso ele seja par, o programa deve calcular o seu quadrado. Mas, se ele for ímpar, deve ser calculado o seu cubo. Ao fim, o programa deve imprimir o valor calculado.#
num1 = int(input("Digite UM numero inteiro: "))
if num1 % 2 == 0: 
   resultado =  num1 **2
else :
    resultado = num1 **3
print(f"O seu resultado é igual a {resultado}")