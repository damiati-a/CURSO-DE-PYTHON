# Uma tabuada que mostre cada valor solicitado, quando indicar um número negativo ele se encerra

while True:
    n = int(input('De qual valor você gostaria de ver a tabuada? '))
    if n < 0:
        break
    print('-'*50)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c} ')
    print('-'*50)
print('PROGRAMA SUPER TABUADAS ENCERRADO!')