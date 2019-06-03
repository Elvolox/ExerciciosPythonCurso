'''from random import randint
from time import sleep
quant = int(input('Quantos jogos você quer?: '))
jogo = []
jogos = []
while True:
    while len(jogo) != 6:
        n = randint(0, 60)
        if n not in jogo:
            jogo.append(n)
    if len(jogos) != quant:
        jogo.sort()
        jogos.append(jogo[:])
        jogo.clear()
    else:
        break
print(f'Sorteando a quanditade de {quant} jogos')
contador = 0
for c in jogos:
    contador += 1
    print(f'Jogo{contador}:{c}')
    sleep(1)'''

#Resposta do professor
from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos jogos você quer?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Sorteadndo {quant} jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

