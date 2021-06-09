#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

print('Programa de escolha de pagamento')
print('''Temos 4 formas de pagamento -
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')

num = int(input('Digite a forma de pagamento: '))
preco = float(input('Qual o valor do produto: R$'))
if num == 1:
    print('Você obteve 10% de desconto por pagar a vista em dinheiro. Valor total pago ser: R${}'.format(preco * 0.9))
elif num == 2:
    print('Você obteve 5% de desconto por pagar. Valor total pago ser: R${}'.format(preco * 0.95 ))
elif num == 3:
    print('Você optou por 2x no cartão. Valor total pago a ser: R${}'.format(preco))
elif num == 4:
    print('Você optou por 3x ou mais no cartão (juros de 20%). Valor total a se pago: R$}'.format(preço * 1.2))
else:
    print('Opção inválida. Tente novamente.')
