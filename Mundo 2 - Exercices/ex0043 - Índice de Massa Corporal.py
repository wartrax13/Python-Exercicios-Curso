from time import sleep
peso = float(input('Qual seu peso? '))
altura = float(input('Qual seu altura? '))
imc = peso / altura ** 2
print('Vamos calcular seu IMC.')
print('Carregando...')
sleep(1)
print('Seu IMC é de {:.2f}'.format(imc))
sleep(1)
if imc < 18.5:
    print('CUIDADO! Você está abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print('Você está com o peso ideal.')
elif imc > 25 and imc <= 30:
    print('Você está em sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você está com obesidade.')
else:
    print('CUIDADO! Você está com Obsidade morbida.')