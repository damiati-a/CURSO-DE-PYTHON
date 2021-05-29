# Catetos e Hipotenusa

co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjascente? '))
hi = (co ** 2 + ca **2) ** (1/2)

print('O comprimento da hipotenusa é {:.2f}'.format(hi))


# ou from math import hypot
import math
co = float(input(' valor do cateto oposto: '))
ca = float(input('valor do cateto adjascente: '))
hi = math.hypot(co, ca)

print('A medida da hipotenusa é {:.2f}'.format(hi))
