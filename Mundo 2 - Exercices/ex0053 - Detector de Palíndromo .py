# uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um polímetro!')
else:
    print('A frase não é um polímetro!')


