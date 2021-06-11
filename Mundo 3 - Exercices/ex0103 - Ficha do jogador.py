#    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#    o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
#    mesmo que algum dado não tenha sido informado

def ficha(nome='sem nome', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s).')

nome = str(input('Qual seu nome? '))
gol = str(input('Quantos gols você fez? '))
if nome == '':
    nome = '<desconhecido>'
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
(ficha(nome, gol))