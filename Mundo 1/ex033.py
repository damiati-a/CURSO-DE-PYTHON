# Ordem, maior e menor valores

a = int(input('Digite um primeiro valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))

# verificando qual o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O menor valor digitado foi: {}'.format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior valor digitado foi {}'.format(maior))
