import datetime
nasc = int(input('Ano de nasc. do atleta: '))
data = datetime.date.today()
anohoje = int(data.strftime('%Y'))
idade = anohoje - nasc

if idade == 20:
    print('Atleta Sênior')
elif idade <= 19:
    print('Atleta Junior, de {} anos'. format(idade))
elif idade <= 14:
    print('Atleta Infantil, de {} anos'.format(idade))
elif idade <= 9:
    print('Atleta Mirim , de {} anos'.format(idade))
elif anohoje > 20:
    print('Atleta master, de {} anos'.format(idade))

print('Fimmmmmmmmmmmm')