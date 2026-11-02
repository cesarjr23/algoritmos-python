nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
    print("Erro: nota inválida.")
else:
    if nota1 >= nota2 and nota1 >= nota3:
        maior = nota1
    elif nota2 >= nota1 and nota2 >= nota3:
        maior = nota2
    else:
        maior = nota3

    if nota1 <= nota2 and nota1 <= nota3:
        menor = nota1
    elif nota2 <= nota1 and nota2 <= nota3:
        menor = nota2
    else:
        menor = nota3

    meio = (nota1 + nota2 + nota3) - maior - menor

    media = ((maior * 5) + (meio * 3) + (menor * 2)) / 10

    if media >= 6:
        print(f"Média: {media:.2f} - APROVADO")
    else:
        print(f"Média: {media:.2f} - REPROVADO")
