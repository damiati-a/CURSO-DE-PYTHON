# JOKENPO

from random import randint
from time import sleep


itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)

print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 3 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

print('=-'*20)
print('{:=^30}'.format(' JO '))
sleep(1)
print('{:=^30}'.format(' KEN '))
sleep(1)
print('{:=^30}'.format(' PO '))
print('=-'*20)

print('-=' * 20)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-=' * 20)

if comp == 0:  # PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 1:  # PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif comp == 2:  # TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
