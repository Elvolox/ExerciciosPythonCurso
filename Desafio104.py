def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digiteum número: ')
print(f'Voce acabou de digitaro o número {n}')
