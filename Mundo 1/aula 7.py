# Adicionando cores ao Python
"""
\033[0; 33; 44m]   # primeiro para estilo, segundo para texto e terceiro para cor de fundo.


STYLE
0 - NONE
1 - BOLD
4 - UNDERLINE
7 - NEGATIVE

TEXT
30 - WHITE
31 - RED
32 - GREEN
33 - YELLOW
34 - BLUE
35 - PINK
36 - CIAN
37 - GREY

BACKGROUND
As mesmas de cima, porém de 40 a 47
"""

# fase prática

# print('\033[7;31;47m Olá, mundo!\033[m')
"""
a = 3
b = 5
print('Os valores são \033[32;40m{} e \033[31;40m{}'.format(a, b))


nome = 'Eu mesmo'
print('ola {}'.format('\033[0;32m', nome, '\033[m'))
"""
# deixar as cores semi prontas

nome = 'André lindão'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('olá, {}{}{}, bem vindo!'.format(cores['azul'], nome, cores['limpa']))
