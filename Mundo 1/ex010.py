# conversor de moedas = 17/02/2021

real = float(input('Qual o valor para conversão? R$ '))

dolar = real / 5.42
euro = real / 6.52
iene = real / 0.051
peso = real / 0.061
bitcoin = real / 283001.17

print('Real: R$ {:.2f}\nDólar: US$ {:.2f}\nEuro: EU$ {:.2f}\nIene Y$ {:.2f}\nPeso: P$ {:.2f}\nBitcoin: B$ {:.5f}'.format(real, dolar, euro, iene, peso, bitcoin))

