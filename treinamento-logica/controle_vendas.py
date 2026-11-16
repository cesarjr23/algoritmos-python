quantidade_vendas = 0
total_vendas = 0
maior_venda = 0

valor_venda = float(input("Informe o valor da venda: "))

while valor_venda != 0:
    if valor_venda < 0:
        print("Venda inválida!")
    else:
        total_vendas += valor_venda
        quantidade_vendas += 1
        if valor_venda > maior_venda:
            maior_venda = valor_venda
    valor_venda = float(input("Informe o valor da venda: "))

if quantidade_vendas > 0:
    media_vendas = total_vendas / quantidade_vendas
    print(f"Quantidade de vendas realizadas: {quantidade_vendas}")
    print(f"Total vendido: R${total_vendas:.2f}")
    print(f"Média das vendas: R${media_vendas:.2f}")
    print(f"Maior venda realizada: R${maior_venda:.2f}")
else:
    print("Nenhuma venda foi registrada!")