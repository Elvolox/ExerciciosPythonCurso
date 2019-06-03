def notas(*n, sit=False):  # Recebendo varias notas
    """
    -> Função para analisar notas e situação de varios alunos
    :param n: Recebendo uma ou mais notas
    :param sit: (OPCIONAL) adiciona a situação na lista e informa se está boa, razoavel ou ruim
    :return: retorna o dicionario
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['media'] > 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
