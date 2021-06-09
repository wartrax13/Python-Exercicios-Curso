#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
from random import randint
lista = []
total = 0
m = 0
cont = menor = 0
barato = ''
while True:
    nome = str(input('Qual é o nome do produto? '))
    preço = float(input('Qual o preço do produto? '))
    total += preço
    cont +=1
    if preço > 1000:
        m += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome

    escolha = str(input('Deseja continuar [S/N]?')).upper()
    if escolha == 'N':
        break

print(f'O total é {total}')
print(f'{m} produto(s) custaram mais de R$1000.')
print(f'O produto mais barato foi {barato} que custa R${menor}.')