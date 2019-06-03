frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

'''inverso = '''    '''Outra forma de fazer'''

'''for letra in range(len(junto)- 1, -1, -1):
   inverso += junto[letra] #Jogando a frase ao contrario'''

if inverso == junto:
    print('Temos um palindromo')
    print(inverso)
else:
    print('Não é palindromo')
    print(inverso)