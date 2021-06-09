#Desafio da tabuada
from time import sleep
print('-=-' * 10)
print('DESAFIO DA TABUADA')
print('-=-' * 10)
sleep(1)
num = int(input('Digite um número da sua tabuada: '))
resultado = 0
for c in range(1, 11):
    resultado = num * c
    print('{} x {} = {}'.format(num, c, resultado))