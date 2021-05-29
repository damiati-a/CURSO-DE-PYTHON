# Analise de triangulos

print('_-_-'*30)
print('Analisador de Triangulos')
print('_-_-'*30)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima FORMAM UM TRIANGULO!')
else:
    print('Os segmentos acima NÃO FORMAM UM TRIANGULO!')
