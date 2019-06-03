km = int(input('Qual a distância da viagem?: '))
# maneira simplificada valor = km * 0.50 if km <= 200 else km * 0.45
if km >= 201:
    valor = km*0.45
    print('Sua é acima de 200km e vai custar: R${}'.format(float(valor)))
else:
    valor =km*0.50
    print('Tem até 200km e vai custar: R${}'.format(float(valor)))

print('Fim')


