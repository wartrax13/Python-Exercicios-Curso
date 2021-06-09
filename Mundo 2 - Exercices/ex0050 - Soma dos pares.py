
#6 numeros inteiros pares para somar
# se não for par, desconsidera.
s = 0
for c in range(0,6):
    n = int(input('Digite seu número: '))
    if n % 2 == 0:
        s += n
    else:
        print('Desconsiderado')
print('{}'.format(s))