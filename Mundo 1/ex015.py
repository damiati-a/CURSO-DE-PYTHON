# Aluguel de carros

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.05)

print('O total a pagar é de R${:.2f}'.format(pago))

