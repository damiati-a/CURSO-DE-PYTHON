# tempo de contagem para fogos de artificio de 10 até 0

from time import sleep

import emoji


print('='*80)
print('VAMOS INICIAR A CONTAGEM REGRESSIVA PARA A VIRADA DO ANO...')
print('='*80)
sleep(2)

print('PREPARADOS?')
sleep(2)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!!!')
print(emoji.emojize(':fireworks:', use_aliases=True))
