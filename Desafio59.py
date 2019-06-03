n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0

while escolha != 5:
    escolha = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] sair do programa
    ######################
    Qual a opção? : '''))

    if escolha == 1:
        r = n1 + n2
        print('A resposta da soma de {} e {} é {}'.format(n1, n2, r))
    elif escolha == 2:
        r = n1 * n2
        print('A resposta da multiplicação de {} e {} é {}'.format(n1, n2, r))
    elif escolha == 3:
        if n1 < n2:
            maior = n2
            print('O maior é o número {}, e o menor é o {}'.format(maior, n1))
        else:
            maior = n1
            print('O maior é o número {}, o menor é o {}'.format(maior, n2))
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor novamente: '))
        n2 = int(input('Digite o segundo valor novamente: '))
    elif escolha == 5:
        print('Você escolheu sair.')
    else:
        print('Opção invalida, ente novamente!')
print('Fim')
