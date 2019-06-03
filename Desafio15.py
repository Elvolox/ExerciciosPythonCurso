dias = int(input("Quantos dias o carro ficou alugado?: "))
KM = float(input("Quantos KM o carro rodou?: "))

pago = (dias*60) + (KM*0,15)
print ("O total a pagar é de R${:.2f}".format(pago))

