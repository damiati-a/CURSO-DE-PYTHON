# Conversor de Temperaturas

cel = float(input('Qual a temperatura agora? °C '))
far = ((9 * cel) / 5) + 32
kel = (cel + 273,15)
print('A temperatura {}°C corresponde à {}°F e em {}°K!'.format(cel, far, kel))

