frase = str(input('Escreva seu nome completo: ')).strip()
dividido = frase.split()
print('O primeiro nome é: ', dividido[0])
print('O último nome é: ', dividido[len(dividido)-1])
