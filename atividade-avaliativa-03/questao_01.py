quant_malabaristas = int(input("Informe a quantidade de malabaristas: "))
soma_notas = 0

while quant_malabaristas <= 0:
    quant_malabaristas = int(input("Informe a quantidade de malabaristas: "))
    
for contador in range(quant_malabaristas):
    nota = float(input(f"Informe a nota do malabarista {contador + 1}: "))
    while nota < 0 or nota > 10:
        nota = float(input(f"Informe a nota do malabarista {contador + 1}: "))

    soma_notas = soma_notas + nota

    if contador == 0:
        menor_nota = nota
        maior_nota = nota
    else:
        if nota < menor_nota:
            menor_nota = nota
        if nota > maior_nota:
            maior_nota = nota
    
media_notas = soma_notas / quant_malabaristas

print(f"A maior nota do campeonato é: {maior_nota:.2f}")
print(f"A menor nota do campeonato é: {menor_nota:.2f}")
print(f"A média geral das notas do campeonato é: {media_notas:.2f}")