#Leia o peso de 5 pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
lista = []
for c in range(0, 5):
    peso = float(input('Qual é o peso? '))
    print('{} kg'.format(peso))
    lista.append(peso)
print('O maior peso foi {} kg'.format(max(lista)))
print('O menor peso foi {} kg'.format(min(lista)))
