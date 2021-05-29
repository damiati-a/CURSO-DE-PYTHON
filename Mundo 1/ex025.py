# lendo um nome de uma pessoa e dizendo se tem SILVA no nome

nome = str(input('Qual o seu nome? ')).strip()

print('Seu nome tem Silva? {}'.format('silva'in nome.lower()))


