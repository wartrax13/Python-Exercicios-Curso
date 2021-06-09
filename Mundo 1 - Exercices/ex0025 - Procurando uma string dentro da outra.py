# - MINHA SOLUÇÃO
# a = input('Digite seu nome: ')
# print('Tem Silva no nome?', 'Silva' in a)

nume = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nume.lower()))