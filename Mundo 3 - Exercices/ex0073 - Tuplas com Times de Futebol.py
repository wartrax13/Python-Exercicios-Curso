#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
times = ('Bragantino', 'Bahia', 'Ceará', 'Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO',
         'Cuiabá', 'Sport', 'Juventude', 'Internacional', 'São Paulo', 'Fluminense', 'Grêmio', 'Atlético-MG',
         'América-MG', 'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos')
print('Os 5 primeiros colocados são: {}'.format(times[:5]))
print('Os 4 ultimos colocados são {}'.format(times[-4:]))
print('Em ordem alfabética: {}'.format(sorted(times)))
