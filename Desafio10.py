real = float(input("Quanto dinheiro você tem na carteira: "))

dolar = real / 3,27

print("Com R${:.2f} você pode comprar apenas US${:.2f}dolares ".format(real, dolar))
