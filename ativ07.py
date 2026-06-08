"""7. Faça um jogo de adivinhação que recebe um número inteiro de 1 a 10 e imprime "Parabéns, você acertou!" caso o jogador acerte o número sorteado pelo programa. Em caso contrário, o jogo imprime "Você errou!" e "Tente um número menor" ou " Tente um número maior" dependendo do valor informado pelo jogador. O jogo deve permitir até 3 chances. Caso o jogador não acerte na terceira vez, o jogo deve imprimir "Você perdeu! Fim de jogo." Dica: Importe a biblioteca random para gerar número aleatório em python e use a função randint(1, 10). Isso retorna um número aleatório entre 1 e 10."""
import random
numero_sorteado = random.randint (1, 10)
chances = 3 
tentativas = 0 
while tentativas < chances:  
    chute = int(input("Digite um número de 1 a 10: "))
    if chute < 1 or chute > 10:
        print("Número inválido! Digite entre 1 e 10.")
        continue
    if chute == numero_sorteado: 
        print("Parabéns , Você acertou!!")
        break
    else: 
        print("Você errou!!")
        if chute < numero_sorteado: 
            print("Tente um número maior!")
        else:
            print("Tente um número menor!")

        tentativas += 1 
        if tentativas < chances: 
            print(f"Você ainda tem {chances- tentativas} chance(s)!")
if chances == tentativas: 
    print(f"Fim de jogo! o nùmero correto era: {numero_sorteado}")