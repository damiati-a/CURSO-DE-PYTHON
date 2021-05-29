# Progressão Aritmética 3.0

print('GERADOR DE P.A.')
print('=-='*10)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('PROGRESSÃO FINALIZADA COM {} TERMOS MOSTRADOS'.format(total))

