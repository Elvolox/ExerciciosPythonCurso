'''#O meu exercicio, correto, porém 17 linhas maior que o do PROF

totpessoas = maispesado = maisleve = 0
dado = []
menorpeso = []
maiorpeso = []
while True:
    nome = (str(input('Digite o nome: ')))
    dado.append(nome)
    totpessoas += 1
    peso = (float(input('Digite o peso: ')))
    dado.append(peso)
    if maisleve == 0:
        maisleve = peso
        menorpeso.append(dado[:])
        dado.clear()
    else:
        if peso == maisleve:
            menorpeso.append(dado[:])
            dado.clear()
        elif peso < maisleve:
            maisleve = peso
            menorpeso.clear()
            menorpeso.append(dado[:])
            dado.clear()
        elif peso > maisleve and maispesado == 0:
            maispesado = peso
            maiorpeso.append(dado[:])
            dado.clear()
        elif peso == maispesado:
            maiorpeso.append(dado[:])
            dado.clear()
        elif peso > maispesado:
            maiorpeso.clear()
            maispesado = peso
            maiorpeso.append(dado[:])
            dado.clear()
    resp = str(input('Você quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
#print(maiorpeso)
print(f'Foram cadastradas {totpessoas} pessoas na lista')
print(f'O menor peso é {maisleve}kg e os papeis são: ', end='')
for mnp in menorpeso:
    print(f'{mnp[0]:.1f}...', end='')
print(f'\nE o maior peso é {maispesado}kg é as baleias são: ',end='')
for maip in maiorpeso:
    print(f'{maip[0]:.1f}...', end='')'''

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
#print(f'Os dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}KG. Peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ', end='')

print(f'O menor peso foi de {men}KG. PEso de ')
for p in princ:
    if p[1] == men:
        print(f'{p[0]} ', end='' )
print()

