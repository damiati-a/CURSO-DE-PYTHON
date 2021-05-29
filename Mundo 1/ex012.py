# Calculo de descontos

pre = float(input('Qual o Preço do produto? R$ '))
novo = pre - (pre * 5 / 100)

print('O produto que custava {:.2f}R$ e com um desconto de 5% vai custa {:.2f}R$'.format(pre, novo))


