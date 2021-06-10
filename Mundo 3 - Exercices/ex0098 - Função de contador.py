'''Faça um programa que tenha uma função chamda contador(), que receba três parâmetros:
'início', 'fim' e 'passo' e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep

def contador(i, f, p):
    if i > f:
        while i > f:
            print(i, end=' ')
            i -= p
            sleep(0.3)
        print('Fim!')
    else:
        while i != f:
            print(i, end=' ')
            i += p
            sleep(0.3)
        print('Fim!')
    print('--' * 20)

print('Contagem de 1 até 10 de 1 em 1')
contador(1, 11, 1)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 1, 2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Escolha o início: '))
f = int(input('Escolha o fim: '))
p = int(input('Escolha os passos: '))
contador(i, f, p)

