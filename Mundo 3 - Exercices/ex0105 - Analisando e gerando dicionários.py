#    Exercício Python 104 - Validando entrada de dados em Python
#    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
#    e vai retornar um dicionário com as seguintes informações:
#       - Quantidade de notas
#       - A maior nota
#       - A menor nota
#       - A média da turma
#       - A situação (opcional)
#    Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
lista = []

def notas(*num, sit=True):
    resp = {'maior': max(lista), 'menor': min(lista), 'tital': len(lista)}
    soma = 0
    soma += num
    sit = soma / len(lista)
    if sit > 5:
        print('Razoável')
    elif sit < 5:
        print('Ruim!')
    elif sit > 7:
        print('Muit bom!')
    #print(f'A quantidade de números foi {len(lista)}')
    #print(f'O maior número foi {max(lista)}')
    #print(f'O menor número foi {min(lista)}')

while True:
    num = float(input('Digite uma nota: '))
    lista.append(num)
    r = str(input('Deseja continuar? [S/N]')).upper()
    if r == 'N':
        soma = 0
        soma += num
        sit = soma / len(lista)
        if sit > 5:
            print('Razoável')
        elif sit < 5:
            print('Ruim!')
        elif sit > 7:
            print('Muit bom!')
        break


notas(num)
