#a = input('Escolha um numero de 1 a 9999: ')
#print('unidade= ', a[3])
#print('dezena= ', a[2])
#print('centena= ', a [1])
#print('milha= ', a[0])

num = int(input('Informe o número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Unidade: {}'.format(d))
print('Unidade: {}'.format(c))
print('Unidade: {}'.format(m))