johnes = 0
pedrao = 0
maluzinha = 0

direcao_perigosa = 0
barulho = 0
bebedeira = 0
heroina = 0

baixo = 0
medio = 0
alto = 0

tipo = int(input("Digite o tipo da ocorrência (1 a 4): "))

while tipo >= 1 and tipo <= 4:

    if tipo == 1:
        direcao_perigosa += 1
    elif tipo == 2:
        barulho += 1
    elif tipo == 3:
        bebedeira += 1
    else:
        heroina += 1

    if tipo == 4:
        gravidade = 3
    else:
        gravidade = int(input("Digite a gravidade (1, 2 ou 3): "))

        while gravidade < 1 or gravidade > 3:
            print("Gravidade inválida!")
            gravidade = int(input("Digite a gravidade (1, 2 ou 3): "))

    if gravidade == 1:
        baixo += 1
    elif gravidade == 2:
        medio += 1
    else:
        alto += 1

    if tipo == 4:
        johnes += 1
        print("Ocorrência atribuída a Johnes.")

    elif johnes <= pedrao and johnes <= maluzinha:
        johnes += 1
        print("Ocorrência atribuída a Johnes.")

    elif pedrao <= maluzinha:
        pedrao += 1
        print("Ocorrência atribuída a Pedrão.")

    else:
        maluzinha += 1
        print("Ocorrência atribuída a Maluzinha.")

    print("\nQuantidade de ocorrências por policial:")
    print(f"Johnes: {johnes}")
    print(f"Pedrão: {pedrao}")
    print(f"Maluzinha: {maluzinha}")

    tipo = int(input("\nDigite o tipo da ocorrência (1 a 4): "))

print("\nTotal de ocorrências por tipo:")
print(f"Direção perigosa: {direcao_perigosa}")
print(f"Barulho: {barulho}")
print(f"Bebedeira: {bebedeira}")
print(f"Heroína: {heroina}")

print("\nTotal de ocorrências por gravidade:")
print(f"Baixo: {baixo}")
print(f"Médio: {medio}")
print(f"Alto: {alto}")
