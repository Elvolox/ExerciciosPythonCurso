dicionario = {}

dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input('Média: '))

'''print(f'O nome é {["Nome"]}')
print(f'A média é {["Media"]}')'''

if dicionario['media'] >= 7:
    dicionario['situação'] = 'Aprovado'
elif 5 <= dicionario['media'] < 7:
    dicionario['situação'] = 'Recuperação'
else:
    dicionario['situação'] = 'Reprovado'

for k, v in dicionario.items():
    print(f'    -{k} é {v}')