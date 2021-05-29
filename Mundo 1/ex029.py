# Radar Eletrônico

# Caso o carro ultrapasse 80 km/h será multado em R$ 7,00 a cada km

velocidade = float(input('Qaula a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado, você excedeu o limite permitido que é de 80 KM/h')
    multa = (velocidade - 80) * 7
    print('Você deverá pagar uma multa de R$ {:.2f}!!'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
