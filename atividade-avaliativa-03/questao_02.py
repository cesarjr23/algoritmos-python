sexo = int(input("Digite o sexo do cliente (1 para feminino ou 2 para masculino): "))

while sexo == 1 or sexo == 2:

    idade = int(input("Digite a idade: "))
    while idade < 18:
        print("Idade inválida!")
        idade = int(input("Digite a idade: "))

    automovel = float(input("Digite o valor do automóvel: "))
    while automovel <= 10000:
        print("Valor inválido!")
        automovel = float(input("Digite o valor do automóvel: "))

    seguro_alfa = automovel * 0.04
    if idade < 30:
        anos_abaixo = 30 - idade
        acrescimo = anos_abaixo * 0.01
        valor_acrescimo = seguro_alfa * acrescimo
        valor_total = seguro_alfa + valor_acrescimo

    elif idade > 50:
        anos_acima = idade - 50
        desconto = anos_acima * 0.01
        if anos_acima >= 15:
            desconto = 0.15
        valor_desconto = seguro_alfa * desconto
        valor_total = seguro_alfa - valor_desconto

    else:
        valor_total = seguro_alfa

    print(f"Valor final do seguro ALFA: R${valor_total:.2f}")


    seguro_beta = automovel * 0.06

    desconto_beta = 0

    if sexo == 1:
        desconto_beta += seguro_beta * 0.05

    if idade >= 30:
        desconto_beta += seguro_beta * 0.10

    valor_total_beta = seguro_beta - desconto_beta

    print(f"Valor final do seguro BETA: R${valor_total_beta:.2f}")


    sexo = int(input("Digite o sexo do cliente (1 para feminino ou 2 para masculino): "))