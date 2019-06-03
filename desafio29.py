velocidade = float((input('Qual a velocidade do carro?: ')))

if velocidade > 80:
    print('Voce foi multado, passou a {}km/h'.format(velocidade))
    multa = (velocidade - 80) * 7
    print('A multa vai lhe custar R${}'.format(multa))

else:
    print('Você não estava acima do limite, não foi multado!')

print('--FIM--')
