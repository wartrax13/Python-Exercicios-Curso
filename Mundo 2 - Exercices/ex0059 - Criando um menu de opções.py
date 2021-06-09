#Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
from time import sleep

print('PROGRAMA DE MENUS')
print('-=-' * 20)
option = 0
n1 = int(input('Escolha o primeiro número: '))
n2 = int(input('Escolha o segundo número: '))
while option != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    option = int(input('Qual sua opção? '))
    if option == 1:
        soma = n1 + n2
        print('Resultado de {} + {} é {}'.format(n1, n2, soma))
        sleep(1)
        print('-=-' * 20)
    elif option == 2:
        produto = n1 * n2
        print('Resultado de {} x {} é {}'.format(n1,n2,produto))
        sleep(1)
        print('-=-' * 20)

    elif option == 3:
        if n1 > n2:
            print('O número {} é maior'.format(n1))
            sleep(1)
            print('-=-' * 20)
        elif n1 == n2:
            print('Os números são iguais!')
            sleep(1)
            print('-=-'*20)
        else:
            print('O número {} é maior'.format(n2))
            sleep(1)
            print('-=-' * 20)
    elif option == 4:
        print('Informe novamente os números:')
        sleep(1)
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))

    elif option == 5:
        print('===FINALIZANDO===')
        sleep(1)
    else:
        print('Tente novamente.')
print('Você saiu do programa!')







