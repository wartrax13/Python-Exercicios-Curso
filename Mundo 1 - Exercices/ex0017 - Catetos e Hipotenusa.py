import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjecente: '))
hi = math.hypot(co, ca)
print('a hipotenusa é {}'.format(hi))