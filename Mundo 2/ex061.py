# Progressão Aritmética 2.0

print('GERADOR DE P.A.')
print('=-='*10)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
