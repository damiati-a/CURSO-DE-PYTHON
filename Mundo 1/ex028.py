# Escreva um programa que o computador pense entre 0 e 5 e veja se o usuario acertou ou não

from random import randint
from time import sleep
comp = randint(0, 5) # Faz o sorteio dos números

print('-=-'*50)
print('Vou pensar num número entre 0 e 5 hein. advinha ai e ganhe um premio!')
print('-=-'*50)
jogador = int(input('Em que número eu pensei? ')) # jogador digita um número

print('PROCESSANDO...')
sleep(3)

if jogador == comp:
    print('Você é o bixão mesmo hein doido, acertou, toma ai o Silvio Santos Pelado. HUMANO 1 PC 0')
else:
    print('Perdeu playboy, eu pensei no {} e não no {}, chupa essa otário. PC 1 HUMANO 0 '.format(comp, jogador))

