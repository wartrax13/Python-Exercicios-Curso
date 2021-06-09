# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.
c = 0
h = 0
m = 0
n = ''

while True:
    idade = int(input('Escolha a idade: '))
    sexo = str(input('Escolha o sexo [M/F]: ')).upper()
    if sexo == 'M':
        h += 1
    elif idade > 18:
        c += 1
    elif sexo == 'F' and idade < 20:
        m += 1
    novo = str(input('Deseja continuar? [S/N]')).upper()
    if novo == 'N':
        print(f'Temos {h} homens cadastrados.')
        print(f'Temos {m} mulheres com menos de 20 anos.')
        print(f'Temos {c} pessoas com mais de 18 anos.')
        break







