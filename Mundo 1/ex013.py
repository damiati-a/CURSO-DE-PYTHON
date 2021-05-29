# Reajuste Salarial

salario = float(input('Qual o salário do funcionário? R$ '))
reajuste = salario + (salario * 30 / 100)

print('O salário do funcionário era de {:.2f}R$ e com o aumento de 30%, agora ele está ganhando {:.2f}R$'.format(salario, reajuste))
