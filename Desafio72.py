numeros = ('zero','um', 'dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove','Vinte')
resp =''
while resp in 'Ss':
    num = int(input('Digite o número que você quer por extenso: '))
    while num > 20 or num < 0:
        num = int(input('Tente novamente, Digite o número que você quer por extenso: '))
    print(f'Voce digitou o numero {numeros[num]}')
    resp = str(input('Voce quer continuar? [S/N]: '))



''' Correção guanabara
cont = ('zero','um', 'dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove','Vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Voce digitou o número {cont[]}')'''



#print(f'Digite o numero que você quer por extenso {numeros[input()]}')