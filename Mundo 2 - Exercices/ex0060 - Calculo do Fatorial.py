# Faça um programa que leia um número e mostre seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 12
# com FOR tbm
#from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print('Calculando {}! = ')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))


'''n = int(input('Digite um número: '))
n1 = n - 1
while n != 1:
    print(n)
    n = n - 1
    soma = n * n

    print(soma)'''


