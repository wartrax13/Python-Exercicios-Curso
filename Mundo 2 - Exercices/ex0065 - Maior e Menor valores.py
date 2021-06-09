#Um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
#O programa deve perguntar ao usuário se ele quer continuar ou não a digitar valores.
import random
x = 0
soma = 0
n = 1
lista = []
while n != 0:
    n = int(input('Digite um número inteiro: '))
    if n > 0:
        x = x + 1
        soma = soma + n
        media = soma / x
        lista.append(n)
        opçao = str(input('Deseja continuar? [S/N]')).upper()
        if opçao == 'S':
            print('Os números foram: {} '.format(lista))
        else:
            print('Os números foram: {} '.format(lista))
            print('O maior numero foi {} kg'.format(max(lista)))
            print('O maior numero foi {} kg'.format(min(lista)))
            print('A media é {} e a soma {}'.format(media, soma))
            print('Obrigado pela atenção!')
            break

