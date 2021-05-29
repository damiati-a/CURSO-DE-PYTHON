# Estatisticas de produtos / simulador de loja

from time import sleep

print('='*30)
print('{:^30}'.format(' LOJÃO DA LÊRERÊ '))
print('='*30)
sleep(3)

total = mil = menor = contador = 0
barato = ' '

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    contador += 1
    total += preco
    if preco > 1000:
        mil += 1
    if contador == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('\n{:-^30}'.format('CAIXA'))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {mil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato da lista foi {barato}')

sleep(3)
print('='*30)
print('{:-^30}'.format('OBRIGADO POR COMPRAR CONOSCO. VOLTE SEMPRE!'))
print('='*30)
