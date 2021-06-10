'''Faça um programa que tenha uma função chamada área(), que receba as dimenções de um terreno
retangular (largura e comprimento) e mostre a área do terreno'''

def area(l,c):
    a = l * c
    print(f'A área é {a}m²')


l = float(input('Qual é a largura? '))
c = float(input('Qual é o comprimento? '))
area(l, c)