r1 = float(input('Digite o número da primeira reta: '))
r2 = float(input('Digite o da segunda: '))
r3 = float(input('E agora o da terceira: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Da para formar um triangulo')
else:
    print('Por favor verificar, pois não há como formar um triangulo!')

if r1 == r2 == r3:
    print('É um triangulo equilatero!!')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('Triangulo isósceles!!')
else:
    print('É um triangulo escaleno!!')
    