# CONDIÇÕES

"""
if e else (se e senão)

se carro.esquerda()
bloco_v_
senão
bloco_f_

correto

if carro.esquerda():
bloco True

else:
bloco False
"""

"""
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')

print('--FIM--')
"""

"""
CONDIÇÃO SIMPLIFICADA

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')
"""

# PARTE PRATICA
"""
nome = str(input('Qual o seu nome?'))
if nome == 'André':
    print('Bem vindo homem mais gostoso da Terra')
    print('Acesso permitido, {}!'.format(nome))
print('Acesso restringido'.format(nome))
"""

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))

if m >= 6.0:
    print('Parabéns, você passou de ano')
else:
    print('Ta mal hein, bora estudar!')
