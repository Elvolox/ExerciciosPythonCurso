from datetime import date
ano = 0
dicionario = {'nome': str(input('Nome: '))}
ano = int(input('Ano de nasc.: '))
datahoje = date.today().year
dicionario['idade'] = datahoje - ano
dicionario['ctps'] = int(input('ctps (número 0 para não tem):'))
if dicionario['ctps'] > 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salario'] = float(input('Salário: '))
    calculoaposentar = datahoje - dicionario['contratação']
    dicionario['aposentadoria'] = calculoaposentar + dicionario['idade']
print('-='*30)
for k, v in dicionario.items():
    print(f'{k} é {v}')

