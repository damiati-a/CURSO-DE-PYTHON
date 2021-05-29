# Seno, Cosseno e Tangente

import math
an = float(input('Digite o angulo que deseja? '))
sen = math.sin(math.radians(an))
print('O angulo de {} tem o seno de {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('O angulo de {} tem o cosseno de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('O angulo de {} tem a tangente de {}'.format(an, tan))

# ou, importando somente os dados utilizaveis. Ai tirando as referencias a 'math'.

from math import radians, sin, cos, tan
