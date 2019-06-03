#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = str(input('Digite uma frase qualquer: ')).upper().strip()

print('Na frase apareceu a letra A por {} vezes, sendo que na primeira vez ela apareceu na posição {} e na ultima vez na posição {}.'.format(nome.count('A'), nome.find('A')+1, nome.rfind('A')+1))