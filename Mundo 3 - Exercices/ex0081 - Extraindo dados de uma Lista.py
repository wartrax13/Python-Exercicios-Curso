'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
des = 'S'
while des == 'S':
    num = (int(input('Digite um valor: ')))
    des = str(input('Deseja continuar? [S/N] ')).upper()
    lista.append(num)

print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'A lista é {lista}')
if 5 in lista:
    print(f'O número 5 está na lista! Apareceu {lista.count(5)}vezes.')
else:
    print('O número 5 não está na lista.')

