import math

n = float(input("Digite um valor: "))

print("O valor digitado {} de forma quebrada ficará {}".format(n, math.trunc(n)))
#ou pode ser usado da forma abaixo sem o modulo math
#print("O valor digitado {} de forma quebrada ficará {}".format(n, int(n)))