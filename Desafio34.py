salario = float(input('Digite o salario do funcionario: '))

if salario >= 1251.00:
    novosalario = salario + ((salario / 100) * 10)
    print('Seu novo salário sera {}'.format(novosalario))
else:
    novosalario = salario + ((salario / 100) * 15)
    print('Seu novo salário será {}'.format(novosalario))