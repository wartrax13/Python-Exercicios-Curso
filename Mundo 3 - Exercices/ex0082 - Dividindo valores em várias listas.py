'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
listapar = []
listaimpar = []

des = 'S'
while des == 'S':
    num = int(input('Digite um valor: '))
    des = str(input('Deseja continuar? [S/N] ')).upper()
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
print(f'A lista completa é {lista}')
print(f'A lista em números pares é {listapar}')
print(f'A lista em números impares é {listaimpar}')
