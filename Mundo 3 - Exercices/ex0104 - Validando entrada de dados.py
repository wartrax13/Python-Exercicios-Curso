

# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(n):
    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            print(f'Você digitou o numero {n}')
            break
        else:
            print('\033[0;31mErro!\033[m')

n = leiaInt('Digite um número: ')