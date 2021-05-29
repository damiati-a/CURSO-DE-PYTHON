# Ordem de precendencia

"""
1 = ()
2 = **
3 = *, /, //, %
4 = +, -
"""

# Exercicios
"""
nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:=^5}!'.format(nome))
"""
n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
i = n1 // n2
e = n1 ** n2
print('A soma {}, o produto é {} e a divisão é{}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potencia {}'.format(i, e))



