from random import randint

num = (randint(1,10), randint(1,10),
       randint(1,10), randint(1,10),
       randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in num: # PRINTA OS NÚMEROS SEM VIRGULA E PARENTES
    print(f'{n} ', end='')
#print (f'Os valores foram {num}')

print(f'\nO maior número foi {max(num)}')
print(f'O menor número foi {min(num)}')