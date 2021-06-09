from random import randint
from time import sleep
print('-=-'* 20)
print('JOKEN PO')
print('-=-'* 20)
print(''' Escolha entre:
[0] pedra
[1] papel
[2] tesoura''')
itens = ('pedra','papel','tesoura')
computador = randint(0,2)

jogador = int(input('Qual é sua jogada? '))

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)

print('-=-'* 20)
print('O computador escolheu: {}'.format(itens[computador]))
print('O jogador jogou: {}'.format(itens[jogador]))
print('-=-'* 20)


if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')
