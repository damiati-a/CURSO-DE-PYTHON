# Aprovação de um empréstimo bancário para uma casa

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário da pessoa: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')
