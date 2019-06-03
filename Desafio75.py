num = (int(input('Digite o primeiro n°: ')),
       int(input('Digite o segundo: ')),
       int(input('O terceiro: ')),
       int(input('O quarto: ')))
print(f'Voce digitou os valores{num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 foi digitado na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

print('\nFim')





