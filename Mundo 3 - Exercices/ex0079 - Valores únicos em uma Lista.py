'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre - os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
lista = []
des = 'S'
while des == 'S':
    num = (int(input('Digite um valor: ')))
    if num not in lista:
        lista.append(num)
    des = str(input('Deseja continuar? [S/N] ')).upper()
lista.sort()
print(lista)




