listanum = []
while True:
    n = int(input('Digite um número: '))
    listanum.append(n)
    resp = str(input('Você quer continuar? [S/N]: '))
    #for pos, cont in enumerate(listanum):
    numerocinco = 0
    if resp in 'Nn':
        break
listanum.sort(reverse=True)
print(f'Foram digitados {len(listanum)} números na lista')
print(f'A lista que foi digitada em ordem decrescente {listanum}')
if 5 in listanum:
    print(f'A lista contem o maldito número cinco')
else:
    print(f'Não tem a merda do número 5 na lista')

