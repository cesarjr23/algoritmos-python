consumo = int(input("Digite o consumo mensal de energia em kWh: "))
bandeira = str(input("Digite a bandeira tarifária (V, A ou R): ").upper())
social = str(input("Inscrito na tarifa social? (S/N): ").upper())

if consumo < 0:
    print("Erro: consumo inválido.")
elif bandeira != "V" and bandeira != "A" and bandeira != "R":
    print("Erro: opção inválida.")
elif social != "S" and social != "N":
    print("Erro: opção inválida.")
else:
    if consumo <=100:
        valor_energia = consumo * 0.60
    elif consumo <= 200:
        valor_energia = (consumo - 100) * 0.80 + (100 * 0.60)
    else:
        valor_energia = (consumo - 200) * 1.10 + (100 * 0.60) + (100 * 0.80)

    if social == "S" and consumo <= 220:
        valor_energia = valor_energia * 0.60

    if social == "S" and consumo <= 220:
        taxa_iluminacao = 0
    else:
        taxa_iluminacao = 12

    if bandeira == "V":
        valor_bandeira = 0
    elif bandeira == "A":
        valor_bandeira = consumo * 0.02
    else:
        valor_bandeira = consumo * 0.05

    total = valor_energia + taxa_iluminacao + valor_bandeira

    print(f"Total a pagar: R$ {total:.2f}")