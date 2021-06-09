from time import sleep
print('Seja bem vinda a mais um desafio! Queremos organizar 3 números entre maiores e menores.')
sleep(1)
a = int(input('Escreva o primeiro numero: '))
b = int(input('Escreva o segundo numero: '))
c = int(input('Escreva o terceiro numero: '))
# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Carregando...')
sleep(2)
print('O menor é {}'.format(menor))
print('Carregando...')
sleep(2)
print('O maior é {}'.format(maior))
