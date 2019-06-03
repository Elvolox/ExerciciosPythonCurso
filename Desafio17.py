import math

co = float(input("Qual o comprimento do cateto oposto: "))
ca = float(input("Qual o do cateto adjacente: "))

##Forma antiga
##hi = (co ** 2 + ca ** 2) ** (1/2)
##print("A hipotenusa vai medir {:.2f}".format(hi))

hi = math.hypot(co, ca)

print("A hipotenusa vai medir {:.2f}", format(hi))