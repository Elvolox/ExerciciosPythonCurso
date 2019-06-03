listage = ('Lápis', 1.75,
           'Borracha', 2,
           'Caderno', 15.90,
           'Estojo', 25)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":40}')#CENTRALIZADO A 40
print('-' * 40)
for pos in range (0, len(listage)):
    if pos % 2 == 0:
        print(f'{listage[pos]:.<30}', end='')
    else:
        print(f'R${listage[pos]:>7.2f}')
print('-' * 40)