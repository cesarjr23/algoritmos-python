nome = str(input("Digite seu nome: "))
horas = float(input("Quantidade de horas trabalhadas: "))
valor = float(input("Valor recebido por hora trabalhada: "))

bruto = valor*horas

if bruto >= 1000:
    desconto = bruto*0.10
else:
    desconto = bruto*0.05

liquido = bruto-desconto

print(f"Funcionário: {nome}")
print(f"Salário bruto: {bruto:.2f}")
print(f"Desconto: {desconto:.2f}")
print(f"Salário líquido: {liquido:.2f}")