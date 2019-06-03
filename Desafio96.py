# minha resposta
def calculoarea(lst):
    area = lst[0] * lst[1]
    print(f'A área de um terreno {lst[0]}x{lst[1]} é de {area}M²')


valores = [float(input('BASE: ')), float(input('Altura:'))]
calculoarea(valores)


# resposta do professor
'''def área(larg, comp):
    a = larg * comp


print('Controle de terrenos')
print('-' * 20)
l = float(input('Largura: '))
c = float(input('Altura: '))
área(l, c)'''
