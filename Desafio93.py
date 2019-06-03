'''jogador = {}
listagols = []
somagol=0
jogador['Nome'] = str(input('NOME: '))
quant = int(input(f"QUANTAS PARTIDAS {jogador['Nome']} FEZ: "))
for c in range(quant):
    gols = (int(input(f'Quantos gols na {c+1}ª partida?: ')))
    somagol += gols
    listagols.append(gols)
jogador['gols'] = listagols
jogador['total'] = somagol
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O {k} tem o valor {v}')
print('-='*30)
print(f"O jogador {jogador['Nome']} jogou {quant} partidas")
print()
for c in range(quant):
    print(f"Na partida {c+1}, ele fez {jogador['gols'][c]} gols.")'''
# Resposta do professor
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range ( 0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' *30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')



