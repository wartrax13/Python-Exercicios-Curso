from datetime import date
print('-=-' * 10)
print('Programa de alistamento militar.')
print('-=-' * 10)
atual = date.today().year
nasc = int(input('Qual o ano do seu nascimento? '))
idade = atual - nasc

if idade == 18:
    print('Está na hora de você se alistar')
elif idade > 18:
    print('Já passou do tempo de você se alistar.')
else:
    print('Ainda faltam {} anos para você se alistar.'.format(18 - idade))
