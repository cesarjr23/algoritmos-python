dia = int(input("Digite o dia do mês (1 a 31): "))
mes = int(input("Digite o mês (1 a 12): "))
ano = int(input("Digite o ano (ex: 2024): "))
data_valida = True

if mes < 1 or mes > 12:
    print("Erro: mês inválido.")
    data_valida = False
if ano <= 0:
    print("Erro: ano inválido.")
    data_valida = False
if dia < 1 or dia > 31:
    print("Erro: dia inválido.")
    data_valida = False

if mes in (4, 6, 9, 11):
    dias_no_mes = 30
elif mes in (1, 3, 5, 7, 8, 10, 12):
    dias_no_mes = 31
elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        dias_no_mes = 29
    else:
        dias_no_mes = 28

if 1 <= mes <= 12 and dia > dias_no_mes:
    print("Erro: dia inválido para o mês informado.")
    data_valida = False

if data_valida:
    if dia < dias_no_mes:
        dia = dia + 1
    else:
        dia = 1
        mes = mes + 1
        if mes > 12:
            mes = 1
            ano = ano + 1

    print(f"Próximo dia: {dia:02d}/{mes:02d}/{ano}")