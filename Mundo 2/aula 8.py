# Condições aninhadas

"""
Diferente da condição nominal, que só pode se ter 2 opções, ou é, ou não é. Esta pode se ter uma terceira opção.
Esta é uma condição dentro de outra condição.

usa-se o uso do comando "senão se" ou "elif"
"""

nome = str(input('Qual é seu nome? '))
if nome == 'André':
    print('Que nomão lindo')
elif nome == 'Pedro' or nome == 'MAria' or nome == 'João':
    print('Nome comum no Brasil fio')
elif nome in 'Ana Josefa':
    print('Nome feio da peste')
# o else é opcional, neste caso.
else:
    print('Nome ok, pode passar.')
print('Tenha um BOm dia {}!'.format(nome))
