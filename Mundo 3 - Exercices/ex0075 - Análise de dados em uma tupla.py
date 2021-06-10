#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
lista = []
v = 0
for c in range(1,5):
    n = int(input('Qual o número? '))
    lista.append(n)
    if n % 2 == 0:
        v += 1
print(f'O número 9 apareceu {lista.count(9)}.')
print(f'O número 3 apareceu na posição {lista.index(3)+1}.')
print(f'Foram digitados {v} números pares.')