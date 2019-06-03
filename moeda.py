def aumentar(preço=0, taxa=0, format=False):
    """
    -> explicação para o código
    :param preço: Recebe o valor float do usuário
    :param taxa: recebe a taxa da porcentagem que altera o preço
    :param format: com True o valor sairá formatado
    :return: retorna o valor junto a formatação ou não
    """
    res = preço + (preço * taxa / 100)
    return res if format is False else moeda(res)


def diminuir(preço=0, taxa=0, format=False):
    res = preço - (preço * taxa / 100)
    return res if format is False else moeda(res)


def metade(preço=0, format=False):
    res = preço / 2
    return res if not format else moeda(res)


def dobro(preço=0, format=False):
    res = preço * 2
    return res if not format else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t\t{moeda(preço)}')
    print(f'Dobro do preço: \t\t{dobro(preço, True)}')
    print(f'Metade do preço: \t\t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preço,taxaa,True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preço,taxar,True)}')
    print('-'*40)


def validação(msg):
    ok = False
    valor = 0
    while True:
        p = str(input(msg))
        if p.isnumeric():
            valor = float(p)
            ok = True
        else:print('\33[0;31mERRO! DIGITE UM VALOR VÁLIDO\033[m')
        if ok:
            break
    return valor