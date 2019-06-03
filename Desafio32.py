from datetime import date
ano = int(input('Digite o ano , ou coloque 0 para analisar o ano anual: '))

if ano == 0:
    ano = date.today().year #Analisando a data de hoje
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))

else:
    print('O ano não é bissexto')