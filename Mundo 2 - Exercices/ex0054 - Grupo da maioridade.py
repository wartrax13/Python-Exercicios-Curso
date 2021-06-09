#crie um programa que leia o ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

x = 0
d = 0
for c in range(0, 7):
    a = int(input('Digite 7 datas de nascimento: '))
    atual = date.today().year
    idade = atual - a
    if idade >= 18:
        print('Atingiu a maior idade')
        x = x + 1
    else:
        print('É menor de idade')
        d = d + 1
print('{} maiores e {} menores'.format(x, d))