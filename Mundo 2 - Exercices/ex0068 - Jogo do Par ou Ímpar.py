# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
d = 0
while True:
    n = int(input('Escolha um número:'))
    comp = randint(1, 11)
    soma = n + comp
    escolha = str(input('Par ou impar? [P/I]')).upper()
    if escolha == 'P' and soma % 2 == 0:
        print(f'Você jogou {n} e o computador escolheu {comp}. Total: {soma}. Deu par!')
        print('Você venceu!')
        print('--' * 20)
        v += 1

    elif escolha == 'I' and soma % 2 != 0:
        print(f'Você jogou {n} e o computador escolheu {comp}. Total: {soma}. Deu impar!')
        print(f'Você ganhou!')
        print('--'*20)
        v += 1
    else:
        print(f'Você jogou {n} e o computador escolheu {comp}. Total: {soma}. Deu impar!')
        print('Você perdeu.')
        print(f'Você venceu {v} vezes')


