preco = float(input('Digite o preço: '))
condicao = int(input('Digite 1 para à vista, ou 2 para parcelar: '))

if condicao == 1:
    tipopagamento = int(input('#############Digite -1- para cartão, ou -2- para dinheiro/cheque#################'))
    if tipopagamento == 1:
        precofinal = preco - (preco * 5 / 100)
        print("o valor final ficará em R${:.2f} com os 5% de desconto.".format(precofinal))
    elif tipopagamento == 2:
        precofinal = preco - (preco * 10 / 100)
        print("O valor final ficará em R${:.2f} com os 10% de desconto".format(precofinal))
elif condicao == 2:
    tipopagamento = int(input('####Digite -1- para parcelar em 2x no cartão, ou -2- para 3x ou mais no cartão########'))
    if tipopagamento == 1:
        precofinal = preco/2
        print('O valor de suas parcelas ficará R${:.2f} em 2x sem juros.')
    elif tipopagamento == 2:
        precofinal = preco + (preco * 20 /100)
        print('O valor final do produto será R${:.2f} com taxa de juros em 20% '.format(precofinal))

        prazo = int(input('Quer parcelar em quantas vezes?: '))
        if prazo >= 3:
            print('O valor ficará em R${:.2f} dividido em {}x.'.format(precofinal/prazo, prazo))
        elif 0 <= prazo <= 2:
            print('Fi duma desgrama, você falo que ia parcelar em 3x ou mais, PULIÇAAAAAAAAAAAAAAAAAAAA!!!')
else:
    print('Opção errada , tente novamente!')