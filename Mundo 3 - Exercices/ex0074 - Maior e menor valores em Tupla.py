#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
lista = randint(0,999)
final = []
for cont in range(0,5):
    lista = randint(0, 999)
    final.append(lista)

print('Os números sorteados foram: {}'.format(final, end=' '))
print((f'O maior número é: {max(final)}'))
print(f'O menor número é: {min(final)}')
#print((min(final)))


#if enumerate(lista) != 5:
    #print(lista)

