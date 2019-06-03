from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
print('Valores sorteados:')
for c in range(0, 4):
    dado = randint(1,6)
    jogo[f'Jogador{c + 1}'] = dado
for k , v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = ()
ranking = sorted(jogo.items(), key=itemgetter(1) , reverse=True)
print('-='*4, 'RANKING', '-='*4)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

