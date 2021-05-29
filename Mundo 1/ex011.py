# calculo de tinta para pintar uma parede, a cada 2 M² para 1l de tinta

larg = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))
area = larg * alt

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(larg, alt, area))

tinta = area / 2

print('Para pintar essa parede, você irá precisar de {}l de tinta'.format(tinta))
