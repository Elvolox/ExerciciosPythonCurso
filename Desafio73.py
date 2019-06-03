brasileirao = ('Atletico','Flamengo','Corinthians','Palmeiras','Fluminense',
 'America-MG','SaoPaulo','Gremio','Vasco da Gama', 'Internacional',
 'Botafogo','Sport Recife','Cruzeiro','EC Vitoria','Santos',
 'Chapecoense','Atletico-PR','Bahia','Ceara SC','Parana')

print(f'Os 5 primeiros são {brasileirao[0:5]}')
print(f'Os 4 ultimos são {brasileirao[-4:]}')
print(f'Os times em ordem alfabética: {sorted(brasileirao)}')
print(f'Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição')
