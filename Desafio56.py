'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = 0
quantidadenova = 0
r = 'S'
'''while r == 'S':'''
for p in range(1, 5):
    print('-------{} Pessoa --------'.format(p))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite a idadade: '))
    sexo = str(input('Digite o sexo M/F: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        quantidadenova += 1



médiaidade = somaidade/4
print('A média de idade do grupo é {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('{} mulheres possuem menos que 20 anos'.format(quantidadenova))
'''r = input('Quer continuar? S/N: ').upper()'''