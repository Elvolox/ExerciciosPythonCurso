soma = 0
num = 0
cont = 0
while True:
    num = int(input('Digite quantos números quiser para somar, ou [999] para parar: '))
    if not num == 999:
        soma += num
        cont += 1
    elif num == 999:
        break
        print('Fim da soma')
        print('###########')

print('Você digitou {} e a soma deu: {} '.format(cont, soma))