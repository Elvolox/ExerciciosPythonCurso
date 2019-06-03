from random import randint
from time import sleep


def sorteio(lst):
    print(f'Sorteando 5 valores: ',end='')
    while len(lst) < 5:
        lst.append(randint(1, 10))
    for v in lst:
        #print(f'Sorteando 5 valores: ')
        print(f'{v} ', end='')
        sleep(0.3)
    print('Fim')


def somapar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'A soma de todos os números PARES de {lst} é {soma}')


numeros = []
sorteio(numeros)
somapar(numeros)
