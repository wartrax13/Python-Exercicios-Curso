#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
cont = 0

while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('--'*20)
    resultado = 0
    if n <= 0:
        break
    for c in range(1, 11):
        resultado = n * c
        print('{} x {} = {}'.format(n, c, resultado))
    print('--'*20)
print('Volte sempre!')
