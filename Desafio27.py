#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome completo: ")).strip()
nome = nome.split()

print('Analisando seu nome...')
print('Seu nome completo é: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
