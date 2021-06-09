from time import sleep
print('Seja bem vinda a mais um desafio!')

a = float(input('Diga a primeira reta do triagulo: '))
b = float(input('Agora a segunda: '))
c = float(input('E a terceira: '))
print('Será que forma um triangulo?')
sleep(2)

if a < b + c and b < a + c and c < a +b:
    print('Sim podemos formar um triangulo.')
else:
    print('Não forma um triangulo')