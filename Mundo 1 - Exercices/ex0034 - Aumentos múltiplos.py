print('Seja bem vindo a mais um desafio!')

salario = float(input('Funcionário, qual seu salário atual? '))
aumento1 = (salario * 1.1) - salario
aumento2 = (salario * 1.15) - salario
if salario > 1250.0:
    print('Seu aumento foi de R${:.2f}'.format(aumento1))
else:
    print('Seu aumento foi de R${:.2f}'.format(aumento2))