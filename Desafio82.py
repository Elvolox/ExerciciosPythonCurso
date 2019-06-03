listanormal = []
listapar = []
listaimpar = []


while True:
    n = int(input('Digite um número inteiro qualquer: '))
    listanormal.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    resp = str(input('Você quer continuar [S/N]?: '))
    if resp in 'Nn':
        break
listanormal.sort()
listapar.sort()
listaimpar.sort()
print(f'A lista normal digitada {listanormal}')
print(f'A lista dos pares {listapar}')
print(f'A lista dos impares{listaimpar}')
