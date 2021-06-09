# import random
#num = str(input('Escolha um número de 1 a 5: '))

#lista = [1, 2, 3, 4, 5]
#escolhido = random.choice(lista)
#if num == escolhido:
#    print('Você acertou')
#else:
#    print('Você errou')
#print('O numero que o PC escolheu foi: ', escolhido)




from random import randint
from time import sleep
computador = randint(1,5) #Faz o computador sortear
print('-=-'*10)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você venceu!')
else:
    print('Você perdeu! Pensei no número {} e não no número {}!'.format(computador, jogador))