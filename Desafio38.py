a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo: '))
c = int(input('E agora o terceiro: '))

maior = a

if a > b and b > c:
    #a , b , c
    print(a,' é o maior valor')
    print(b, 'é o segundo maior valor')
elif a < b and b < c:
    #c , b , a
    print(c , 'é o maior valor')
    print(b, 'é o segundo maior valor')
elif a > b and b < c:
    # a , c , b
    print(a,'é maior valor')
    print(c, 'é o segundo maior valor')
elif b > c and b > a:
    # b , c , a
    print(b,'é o maior valor')
    print(c,'é o segundo maior valor')
elif b > a and c < a:
    print(b,'é o maior valor')
    print(a,'é o segundo maior valor')
    #b, a, c
elif c > a and a < b:
    # c, a, b
    print(c, 'é o maior valor')
    print(a, 'é o segundo maior valor')

else:
    print('Todos os valores são iguais')

print('Fimmmmmmmm')




print('------------------------------------Fim----------------------------------------')