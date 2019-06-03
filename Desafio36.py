salario = float(input('Digite seu salario: '))

rendaminima = salario*30/100

print('######Atenção###########!!!')
print('O valor da prestação não pode passar de R${:.2f}'.format(rendaminima))

vcasa = float(input('Digite o valor da casa: '))
anos = float(input('Digite a quantidade de anos que vc quer parcelar: '))

meses = anos*12
prestacao = vcasa/meses



if rendaminima >= prestacao:
    print('Aprovado! Prestação de R${:.2f} dentro do permitido, de R${:.2f} que você pode pagar'.format(prestacao, rendaminima))
else:
    print('Emprestimo negado, pois a prestação de R${:.2f} excedeu o limite de 30% que seria R${:.2f} de sua renda!'.format(prestacao, rendaminima))



print('Fimmm----------')