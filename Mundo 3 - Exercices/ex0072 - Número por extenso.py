#Crie um programa que tenho uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.

name = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oite', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
if n <= 20:
    print(name[n])
else:
    print('Você digitou errado. Tente de novo, de 0 a 20')
