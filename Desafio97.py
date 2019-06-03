# MINHA RESPOSTA
'''def titulo(txt): # Defina titulo no txt
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))

titulo('Augusto')
titulo('viado')
titulo('Esse exercicio é muito baba')'''

#RESPOSTA DO PROFESSOR

def titulo(txt): # Defina titulo no txt
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)

titulo('Augusto')
titulo('viado')
titulo('Esse exercicio é muito baba')