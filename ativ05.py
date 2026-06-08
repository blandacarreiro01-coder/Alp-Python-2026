"""5. Crie um programa no qual o usuário informe 2 números inteiros: a e b. Para que o programa continue sua execução, verifique se a < b. Se sim, calcule a soma dos números inteiros no intervalo [a, b]. Caso contrário, informe uma mensagem de erro."""
num1 = int(input("Digite o número a: "))
num2 = int(input("Digite o número b: "))
if num1 < num2:
    soma = 0
    for contange in range(num1, num2 +1):
         soma += contange
    print(f"A soma do intervalo [{num1}, {num2}] é {soma}")

else:
    print("ERRO! a deve ser menor que b.")
         
