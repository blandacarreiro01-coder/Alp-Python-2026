import random
nomes = []

print("=== RIFA DA FORMATURA ===")
print("Digite 'fim' para encerrar o cadastro.\n")

while True:
    nome = input("Nome do comprador: ").strip()
    if nome.lower() == "fim":
        break
    if nome == "":
        print("Nome inválido. Tente novamente.")
        continue
    nomes.append(nome)
    print(f"  '{nome}' cadastrado!")

if len(nomes) == 0:
    print("\nNenhum participante cadastrado. Sorteio cancelado.")
else:
    print(f"\nTotal de participantes: {len(nomes)}")
    print("Participantes:", nomes)
    ganhador = random.choice(nomes)
    print(f"\n O ganhador da rifa é: {ganhador} 🎉")