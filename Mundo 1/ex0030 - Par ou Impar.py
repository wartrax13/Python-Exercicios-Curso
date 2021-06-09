#programa de ler um numero inteiro e mostrar na tela se ele é PAR ou IMPAR.
print('Seja bem vinda a mais um desafio!')
num = int(input('Digite um numero para ver se é PAR ou IMPAR: '))
impar = (num -1)
resultado = num % 2
if resultado == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))