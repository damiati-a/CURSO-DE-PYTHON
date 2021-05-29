# Simulador de caixa eletrônico

print('='*60)
print('{:^60}'.format('BANCO POBRETÃO'))
print('='*60)

valor = int(input('Qual o valor que você gostaria de sacar? R$ '))
total = valor
cedula = 200
totalcedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        print(f'TOTAL DE {totalcedulas} CÉDULAS DE R$ {cedula}')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totalcedulas = 0
        if total == 0:
            break

print('='*60)
print('É UM PRAZER FAZER NEGÓCIOS COM VOCÊ. VOLTE SEMPRE!')
print('='*60)
