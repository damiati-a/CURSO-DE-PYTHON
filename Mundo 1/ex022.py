# Analisador de textos

nome = str(input('Digite seu nome completo: ')).strip()   # .strip para tirar os espaços na leitura

print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))  # nome.count(' ') tirando os espaços do meio

# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))   ou outra maneira mais completa abaixo

separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))



