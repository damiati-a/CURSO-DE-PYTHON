# maior e menor da sequencia

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O Maior peso apresentado foi {} '.format(maior))
print('O Menor peso apresentado foi {} '.format(menor))

