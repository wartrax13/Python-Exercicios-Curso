#Faça um programa que programe o computador a pensar um numero de 0 a 10
#e que leia seu numero até você acertar o numero que o computador escolheu.
from random import randint
'''comp = randint(0, 10)
n = 0
while n != comp:
    n = int(input('Escolha seu número: '))
    if n != comp:
        print('Você errou! Tente novamente')
    else:
        print('Você acertou!')'''
computador = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou com {} tentativas! Parabéns!'.format(palpites))

