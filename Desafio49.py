n = int(input("Digite o valor da sua tabuada"))
for t in range(1 , 11):

    print("=" * 12)
    print('{} x {:2} = {}'.format(n, t, n * t))


