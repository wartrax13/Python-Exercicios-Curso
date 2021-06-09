import math
angulo = float(input('digite o angulo que você quer: '))
seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print('o angulo de {} tem o coseno de {:.2f}'.format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))
