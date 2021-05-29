# jogo da adivinhação 2.0

from random import randint

computador = randint(0, 10)
print('Vamos jogar um jogo? Dúvido acertar um número que eu estou pensando. Entre 0 e 10')


acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais pra cima Amigão...')
        elif jogador > computador:
            print('Mais pra baixo Amigão...')

print('Acertou com {} tentativas. Parabéns. Tu é o bixão memo hein.'.format(palpites))

