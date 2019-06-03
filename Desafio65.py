r = 'S'
maior = menor = media = soma = quantidade = 0

while r in 'Ss':
    num = int(input('Digite um numero inteiro: '))
    soma += num
    quantidade += 1
    r = str(input('Você quer continuar S/N?: ')).upper().strip()[0]

    if quantidade == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if maior < menor:
            menor = num
media = soma / quantidade

print('Voce digitou {} numeros e a média é {}, o maior número foi {} e o menor foi {}'.format(soma, media, maior, menor))