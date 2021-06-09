#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
#Caso esteja errado, peça a digitação novamente.

def obter_sexo():
    while True:
        n = str(input('Digite [M] para masculino e [F] para feminino: ')).upper()
        if n in ['MASCULINO','FEMININO']:
            return n
        else:
            print('Escolha errada.')
template = '''Você escolheu:



{sexo}'''

if __name__ == '__main__':
    letra = 'M'
    print(template.format(sexo = letra))

