#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.
from time import sleep
print('Seja bem vinda a mais um desafio!')
sleep(1)
km = float(input('Quando em Km você viajou? '))
price1 = km * 0.5
price2 = km * 0.4
if km > 200:
    print('Que viagem longa! Você pagou R${}'.format(price2))
else:
    print('Que viagem curta! Você pagou R${}'.format(price1))