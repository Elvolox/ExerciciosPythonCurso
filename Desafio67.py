while True:
    print("-" * 5)
    num = int(input('Digite o valor da tabuada: '))
    print("-" * 5)
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} * {c} é igual a {num*c}')
print('TABUADA ENCERRADA MEEEEN, VOLTE SEMPRE!!!')