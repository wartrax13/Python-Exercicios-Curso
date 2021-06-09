from time import sleep
print('-=-'* 10)
vel = float(input('Qual velocidade está o carro? '))
print('Calculando...')
sleep(2)
multa = (vel - 80) * 7
if vel > 80:
    print('MULTADO! Ultrapassou o limite de 80 km/h. Sua multa é de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia!')