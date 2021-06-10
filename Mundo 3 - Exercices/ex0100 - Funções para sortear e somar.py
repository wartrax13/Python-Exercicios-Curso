'''Faça um programa que tenha uma lista chamada 'números' e duas funções chamada sorteia() e somaPar().
 A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
 a soma entre todos os valores PARES sorteados pela função anterior.'''
from random import randint
from time import sleep
numeros = list()
def sorteia(numeros):
    print('Sorteando 5 valores da lista.')
    for cont in range(0,5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)

    print(f'Pronto')

def somaPar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando as valores pares de lista {numeros}, temos {soma}')


sorteia(numeros)
somaPar(numeros)