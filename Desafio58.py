import random

numero = int(input('Digite um numero de 0 a 10: '))
numeroc = random.randint(0,10)
palpite = 0

while not numero == numeroc:
    print('Que pena , você errou, seu número {} não é igual da maquina {}'.format(numero, numeroc))
    print('#'*5)
    numero = int(input('Digite um numero de 0 a 10: '))
    numeroc = random.randint(0,10)
    palpite += 1

if numero == numeroc:
    print('Voce acertou o número que a maquina pensou, sou número foi {} e o da maquina foi {}'.format(numero, numeroc))
    print('Foram precisos {} palpites para vencer a maquina.'.format(palpite))

