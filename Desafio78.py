lista = []
maiornum = 0
menornum = 0
for c in range (0, 5):
    lista.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maiornum = menornum = lista[c]
    else:
        if lista[c] > maiornum:
            maiornum = lista[c]
        if lista[c] < menornum:
            menornum = lista[c]

print(f'O maior valor digitado foi {maiornum} nas posições ', end='')
for pos, conteudo in enumerate(lista):
    if conteudo == maiornum:
        print(f'{pos}... ', end='')
print()
print(f'O menor valor digitado foi {menornum} nas posições ', end='')
for pos, conteudo in enumerate(lista):
    if conteudo == menornum:
        print(f'{conteudo}... ', end='')
print()
