#Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúsculas
#o nome com todas as letras minúsculas
#Quantas letras ao (todo sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("O seu nome em letras minusculas: {}" .format(nome.lower()))
print("O seu nome em letras maiúsculas: {}". format(nome.upper()))
print("Seu nome possui {} letras". format(len (nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #buscando o primeiro espaço para poder contar os caracteres até ele, considerando o .strip()
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))