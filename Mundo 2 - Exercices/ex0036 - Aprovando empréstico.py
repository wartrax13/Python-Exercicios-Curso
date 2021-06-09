#Programa para empréstimo de uma casa
from time import sleep
print('-'* 20)
print('Bem vindo!')
print('Programa de avaliação de emprestimo!')
print('-'* 20)

valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos quer pagar? R$'))
meses = anos * 12
pres = (valor / meses)
sleep(1)

if pres >= salario * 0.3:
    print('Você não tem condições para comprar essa casa em tantos meses.')
    sleep(1)
    print('Nessas condições, o valor de cada parcela seria R${:.2f}'.format(pres))
    sleep(1)
    print('Tente parcelar em mais vezes.')
    sleep(1)
    print('Sugestão: {:.0f} meses.'.format(valor / (salario * 0.3)))
    sleep(1)
    print('Ou melhor, aproximadamente {:.0f} anos.'.format((valor / (salario * 0.3) / 12)))

else:
    print('Parabéns! Você tem condições para comprar a casa.')
    sleep(1)
    print('Nessas condições, para uma casa de R${}, para ser paga em {} anos, o valor de cada parcela seria R${:.2f}'.format(valor,anos, pres))



