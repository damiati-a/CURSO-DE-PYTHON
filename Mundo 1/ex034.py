# Aumento de salários

salario = float(input('Qual é o salário do funcionário? R$ '))

if salario <= 2000:
    novo = salario + (salario * 25 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Quem ganhava {} R$, passará a ganhar {} R$ agora. '.format(salario, novo))
