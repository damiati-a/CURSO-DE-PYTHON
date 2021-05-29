# QUEBRANDO UM NÚMERO

# 3 maneiras

import math
num = float(input('Digite um valor: '))
print('O valor digitado {} e a sua porção inteira é {}'.format(num, math.trunc(num)))


from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado {} e a sua porção inteira é {}'.format(num, trunc(num)))


num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua poção inteira é {}'.format(num, int(num)))
