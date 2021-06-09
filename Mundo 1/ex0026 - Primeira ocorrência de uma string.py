frase = input('Escreve uma frase: ').strip()
print('Quantas vezes aparece a letra A?', frase.upper().count('A'))
print('E que posição a primeira vez? ', frase.upper().find('A'))
print('E a última vez?', frase.upper().rfind('A'))

