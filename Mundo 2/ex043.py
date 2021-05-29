# Indice de massa corporea (IMC)

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é  de {:.1f}!'.format(imc))

if imc < 18.5:
    print('Você está abaixo da faixa de Peso Normal')
elif 18.5 <= imc < 25:
    print('Você está na faixa de Peso Normal')
elif 25 <= imc < 30:
    print('Você está na faixa de Sobrepeso')
elif 30 <= imc < 40:
    print('Você está Acima do Peso Normal (Obesidade)')
elif imc >= 40:
    print('Você está muito acima da faixa Normal de Peso (Obesidade Mórbida)')

print('\nCUIDE SEMPRE DA SUA SAÚDE!')