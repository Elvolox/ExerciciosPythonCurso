import random

pa = input("Primeiro Aluno: ")
sa = input("Segundo Aluno: ")
ta = input("Terceiro Aluno: ")
qa = input("Quarto Aluno: ")

list = [pa, sa, ta, qa]
escolhido = random.choice(list)

print("O Aluno escolhido foi: {}".format(escolhido))
