''' MINHA RESPOSTA QUASE CERTA
somapares = somaterceiracoluna = 0
maiornum = []
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range (0,3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for p in matriz:
    for n in p:
        if n % 2 == 0:
            somapares += n
for p in matriz:
    somaterceiracoluna += p[2]
for p in matriz:
    #print(p[1])
    maiornum.append(p[1])
maiornum.sort()
print(f'Soma dos pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {somaterceiracoluna}')
print(f'O maior número da segunda linha é o nº{maiornum[2]}')'''

#RESPOSTA DO PROF
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range (0,3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[1][c]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz [1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')