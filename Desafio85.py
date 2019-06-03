''' ESTA CERTO MAIS O PROF PEDIU MAIS SIMPLIFICADO AINDA
listapar = []
listaimpar = []
principal = []
for c in range (1,8):
    principal.append(int(input(f'Digite o {c}º valor: ')))
for p in principal:
    if p % 2 == 0:
        listapar.append(p)
    else:
        listaimpar.append(p)
print(principal)
listapar.sort()
listaimpar.sort()
print(listapar)
print(listaimpar)'''

#RESPOSTA DO PROFESSOR
num = [[], []]
valor = 0
for c in range (1, 8):
    valor = int(input('Digite um número: '))
    if valor % 2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(num[0])
print(num[1])

