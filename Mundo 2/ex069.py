
# Análise de dados do grupo

from time import sleep

print('--- BEM VINDO AO CADASTRO DO IBGE ---')
sleep(2)
print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)

t18 = thomem = tmulher = 0

while True:
    idade = int(input('Informe uma idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe uma sexo [M/F]: ')).strip().upper()
    if idade >= 18:
        t18 += 1
    if sexo == 'M':
        thomem += 1
    if sexo == 'F' and idade < 20:
        tmulher += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja cadastrar mais pessoas?[S/N] ')).strip().upper()
    if resposta == 'N':
        break

print(f'O Total de pessoas com mais de 18 anos cadastradas foi de: {t18}.')
print(f'Ao todo temos {thomem} homens cadastrados.')
print(f'E temos {tmulher} mulheres com menos de 20 anos cadastradas.')