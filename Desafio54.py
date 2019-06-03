from datetime import date
totmaior = 0
totmenor = 0
atual = date.today().year

for c in range(0, 7):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(totmaior, 'São maiores, e', totmenor, 'São menores')