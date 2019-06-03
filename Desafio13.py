salario = float(input("Qual o salário do funcionario?: "))

novosalario = salario + (salario * 15 / 100)

print("Um funcionário que ganhavaR${:.2f}, com 15% de aumento, passará a ganhar R${:.2f}.".format(salario, novosalario))