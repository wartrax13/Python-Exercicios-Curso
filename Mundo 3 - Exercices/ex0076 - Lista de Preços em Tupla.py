#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('Pão', 1,
            'Ovo', 12,
            'Leite', 3,
            'Arroz', 13,
            'Tomate', 5)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

print('--'*20)
print('LISTAGEM DE PREÇOS')
print('--'*20)
#print(f'O {listagem[0]} ------ R${listagem[1]:.2f}')
#print(f'O {listagem[2]} ------ R${listagem[3]:.2f}')
#print(f'O {listagem[4]} ---- R${listagem[5]:.2f}')
#print(f'O {listagem[6]} ---- R${listagem[7]:.2f}')
#print(f'O {listagem[8]} --- R${listagem[9]:.2f}')

