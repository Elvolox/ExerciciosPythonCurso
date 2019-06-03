import random
numero = int(input('Digite um numero de 0 a 5: '))
numeroc = random.randint(0,5)


if numero == numeroc:
    print('Voce acertou o número que a maquina pensou, sou número foi {} e o da maquina foi {}'.format(numero, numeroc))

else:
    print('Que pena , você errou, seu número {} não é igual da maquina {}'.format(numero, numeroc))