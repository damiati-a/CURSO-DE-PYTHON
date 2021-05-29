# soma de multiplos de 3

soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont += 1  # += significa que cont recebe cont + 1
        soma += num
        print(num)
print('A soma ded todos os {} valores solicitados foram {}'.format(cont, soma))
