'''Crie um programa que tenha uma função chamada voto()
que vai receber como parametro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto negado, opcional
ou obrigatório nas eleções.'''
from datetime import date
def voto(ano):
    atual = date.today().year
    x = atual - ano
    if x == 16 or x == 17 or x >= 60:
        return f'Com {x} anos o vote é opcional.'
    elif x >= 18:
        return f'Com {x} anos o voto é obrigatório. '
    else:
        return f'Com {x} anos não vota!'
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
