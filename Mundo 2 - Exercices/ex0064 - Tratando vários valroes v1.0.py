#Programa que leia vários numéros até 999.
#Quando ler 999, o programa vai parar e falar a quantidade de números que foram digitados e sua soma.

num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print('Fim com soma de {} e {} números'.format(soma, cont))