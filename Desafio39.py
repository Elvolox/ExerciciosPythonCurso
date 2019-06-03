import datetime
nasc = int(input("Digite seu ano de nascimento: "))
data = datetime.date.today()
ano = int(data.strftime('%Y'))

if (2019-nasc) == 18:
    print("Vá se alistar!")
elif (2019-nasc) > 18:
    excedido = (ano - nasc) - 18
    print("Ja passou {} anos do tempo do alistamento, o camburão vai te pegar!".format(excedido))

else:
    print('Você ainda não tem a idade minima requerida!')
    previsao = ano - nasc
    print('Faltam {} anos para o dia do alistamento'.format(previsao))

print ('Fimmmm!!!')