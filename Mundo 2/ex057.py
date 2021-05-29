# validação de dados com while

# registro do sexo da pessoa, só aceita M ou F

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos, digite novamente, utilizando apenas [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

