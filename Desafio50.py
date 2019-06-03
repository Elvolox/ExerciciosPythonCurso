soma = 0
cont = 0
for c in range(1,7):
    num = int(input("Numero {}: ".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1

print(cont, soma)

print('Foi informado {} números pares e a soma deu {}'.format(cont,soma))
