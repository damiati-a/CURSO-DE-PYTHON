# maior e menor valores, calculo de média


quantidade = soma = maior = menor = 0
continuar = 'S'

while continuar == 'S':
    num = int(input('Digite um numero: '))
    if quantidade == 0:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    soma += num
    quantidade += 1

    continuar = str(input('Que continuar? [S/N] ')).upper().strip()
    media = soma / quantidade

print('A media dos {} valores digitados foi de {}'.format(quantidade, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))


"""
print(f'\nA media dos {quantidade} valores digitados foi {soma / quantidade}\n'  # ao invés de usar .format
      f'O maior valor digitado foi {maior} e o menor foi {menor}')
"""