# conversor de medidas em metro

medida = float(input('Digite uma distancia em metros: '))
ja = medida * 0.9144
cm = medida * 100
mm = medida * 1000
km = medida * 0.001
ma = medida * 1609.34
print('Seu valor é {:.0f}cm e {:.0f}mm, {:.0f}ja, {:.0f}km, {:.0f}ma'.format(cm, mm, ja, km, ma))


