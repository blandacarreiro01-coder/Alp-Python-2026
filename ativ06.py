"""6. Um professor de Matemática deseja construir um programa para imprimir uma Progressão Aritmética (PA). Para isso, devem ser informados 3 argumentos: a) primeiro termo, b) quantidade de termos e c) razão."""
primeiro = int(input("Digite o primeiro termo da PA: "))
quantidade = int(input("Digite a quantidades de termos da PA:  "))
razão = int(input("Digite a razão da PA: "))

print("PA:", end=" ")
i = 0   
while i < quantidade:
    termo = primeiro + i * razão
    if i < quantidade - 1: 
        print(termo , end=",")
    else: 
        print(termo)
    i += 1