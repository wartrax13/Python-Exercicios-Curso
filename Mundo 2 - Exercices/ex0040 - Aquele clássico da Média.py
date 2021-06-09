from time import sleep
print('Calculadora escolar!')
print('--'* 20)
sleep(1)
a = float(input('Qual sua primeira nota? '))
b = float(input('Qual sua segunda nota? '))
media = (a + b) / 2
if media >= 7.0:
    print('Sua média é: {}'.format(media))
    sleep(1)
    print('Você foi APROVADO.')

elif media < 5.0:
    print('Sua média é: {}'.format(media))
    sleep(1)
    print('Você foi reprovado.')

elif media >= 5 and media < 7:
    print('Sua média é: {}'.format(media))
    sleep(1)
    print('Você está de recuperação.')
