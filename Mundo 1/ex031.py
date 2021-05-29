# calculando o custo de uma viagem de acordo com a distancia

dist = float(input('Qual a distância da sua viagem? '))
print('Você fará uma viagem de {} KM.'.format(dist))


if dist <= 200:
    preco = dist * 0.50

else:
    preco = dist * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))


# outra maneira
"""
dist = (float(input('Qual a distancia da sua viagem: ')))
print('VOce fará uma viagem de  {:.2f} KM.'.format(dist))

preco = dist * 0.50 if dist <= 200 else dist * 0.45
print('O preço da sua passagem será de {:.2f}'.format(preco))
"""