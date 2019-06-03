listanum = []
varificador = 0
while True:
    n = int(input('Digite um número: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adcidionado com sucesso!!!')
    else:
        print('O valor ja está na lista, não vou adicionar')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
listanum.sort()
print(f'Os valores adicionados foram {listanum}')