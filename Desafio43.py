peso = float(input('Peso: '))
altura = float(input('Altura: '))

alturaq = (altura*altura)
imc = peso/alturaq
if imc < 18.5:
    print('Você ta abaixo do peso papi! IMC:{}'.format(imc))
elif 18.5 <= imc <= 25.0:
    print('Peso ideal papi! IMC:{}'.format(imc))
elif 25.1 <= imc <= 30.0:
    print('Sobre peso, IMC:{}!!'.format(imc))
elif 30.1 <= imc <= 40.0:
    print('obesidade! IMC:{}'.format(imc))
elif imc >= 40.1:
    print('Se vai morrer! IMC:{}'.format(imc))

print('fim!!!')
