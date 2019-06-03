'''while True: # ESTAVA INDO NO CAMINHO CERTO MAIS ERREI NO LAÇO ERRAAAAADOO
    tipo = ''

    while tipo in 'S':
        sexo = str(input('Digite o sexo M/F: ')).upper().strip()[0]
        idade = int(input('Digite a idade: '))
        tipo = str(input('Você quer continuar [S/N]: ')).upper().strip()[0]
        contador1 = 0
        contador2 = 0
        contador3 = 0
    if idade >= 18:
        contador1 += 1

    if sexo == 'M':
        contador2 += 1

    if sexo == 'F' and idade < 20:
        contador3 += 1

    if tipo not in 'S':
        break
print(f'Tem {contador1} pessoas > 18, tem {contador2} homens e {contador3} Mulheres < 20')'''

# CODIGO CORRETO A BAIXO

tot18 = totH = totM20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]

    if idade >= 18:
        tot18 += 1

    if sexo == 'M':
        totH += 1

    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]#[0]PEGA SO A PRIMEIRA LETRA
    if resp == 'N':
        break

print(f'Total de pessoasl com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
