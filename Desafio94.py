pessoas = {}
listageral = []
somaidades = mediaidades = 0
while True:
    pessoas['nome'] = str(input('Nome: ').upper())
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Verifique a digitação, apenas [M/F]')
    pessoas['idade'] = int(input('Idade: '))
    somaidades += pessoas['idade']
    listageral.append(pessoas.copy())
    while True:
        resp = str(input('Continuar [S/N]?: ')).upper().strip()[0]
        if resp in 'SsNn':
            break
        print('Erro, verifique a digitação, apenas [S/N]')
    if resp == 'N':
        break

print(f'Ao todos temos {len(listageral)} pessoas cadastradas')
mediaidades = somaidades / len(pessoas)
print(f'A média de idade é de {mediaidades:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in listageral:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas acima da média: ', end='')
for p in pessoas:
    if p['idade'] >= mediaidades:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('FIMMMM DO PROGRAMAAAA')