
soma = menorpreço = maisdemil = 0
nomeproduto = ' '

while True:
    nomeproduto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço: '))
    soma += preço

    resp = ' '

    if menorpreço == 0:
        menorpreço = preço
    elif menorpreço > preço:
        menorpreço = preço
        maisbarato = nomeproduto
    if preço > 1000:
        maisdemil += 1


    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total casto na compra: {soma:.2f}')
print(f'Até agora o produto mais barato é {maisbarato} custando {menorpreço:.2f}')
print(f'Total de produtos custando mais de 1k: {maisdemil}')
