'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''
lista = []
def maior(*num):
    print(num)
    print(f'Foram informados {len(num)} números. O maior deles é {max(num)}')

maior(1, 2, 4, 6, 7, 3, 5, 10)