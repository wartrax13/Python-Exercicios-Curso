from time import sleep
from datetime import date
print('-=-' * 10)
print('Confederação Nacional de Natação: categorias')
print('-=-' * 10)
sleep(1)
atual = date.today().year
a = int(input('Insira seu ano de nascimento: '))
idade = atual - a
print('Sua idade é {}'.format(idade))
sleep(1)
if idade <= 9:
    print('Você pertence a categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print('Você pertence a categoria INFANTIL.')
elif idade > 14 and idade <= 19:
    print('Você pertence a categoria JUNIOR.')
elif idade > 19 and idade <= 25:
    print('Você pertence a categoria SÊNIOR.')
else:
    print('Você pertence a categoria MASTER.')

