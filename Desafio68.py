#PAR OU IMPAR PARRUDO!
import random
v =0
while True:
    numjogador = int(input('Digite um número de 1 a 10 para somar com o computador: '))
    numerocomputador = random.randint(0, 10)
    resultado = numerocomputador + numjogador
    tipo = ''

    while tipo not in 'PI':
        tipo = str(input('Par ou impar?[P/I] ')).strip().upper()[0]
    print(f'O computador jogou {numerocomputador} e você jogou {numjogador}' , end='')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU IMPAR' )
    if tipo == 'P':
        if resultado %2 == 0:
            print('Voce venceu!!')
            v += 1
        else:
            print('Voce perdeu!!')
            break
    elif tipo == 'I':
        if resultado % 2 == 1:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
print('Fimmmmm')



