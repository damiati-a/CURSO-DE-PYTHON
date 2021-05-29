"""
n1 = int(input('Digite um Número:'))
n2 = int(input('Digite um Número:'))
s = n1 + n2  # '+' serve como concatenação. Para adição precisa-se converter para Int (inteiro).
# print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
print('A soma vae {}'.format(s))
print(type(n1))
"""

'''
Tipos Primitivos
1
int  = 7, -4, 0, 1231231
float  = 4.5, 0.0034, -13.332, 7.0  -> números reais
bool  = True or False
str  = 'olá', '7.5', '' -> Tudo entre aspas é considerado String
'''

# DESAFIO
n1 = int(input('número 1: '))
n2 = int(input('Número 2: '))
s = n1 + n2
print('A soma de {} e {} é? {}'.format(n1, n2, s))


