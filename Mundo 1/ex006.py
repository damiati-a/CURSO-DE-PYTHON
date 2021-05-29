# Dobro, triplo e raíz quadrada

n = int(input('Digite um número: '))
print('o dobro deste número é {}, o triplo {} e a raíz quadrada {}'.format((n * 2), (n * 3), (n ** (1 / 2))))


# forma mais comum
"""
n = int(input('digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('o dobro deste número é {}'.format(d))
print('o triplo é {} \na raíz quadrada é {:.2f}'.format(t, r))
"""

# pode-se usar  'pow(n, (1/2))' para raíz quadrada

