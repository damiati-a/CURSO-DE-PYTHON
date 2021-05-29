# Sorteio de uma ordem

from random import shuffle
nome1 = str(input('Primeiro grupo: '))
nome2 = str(input('Segundo grupo: '))
nome3 = str(input('Terceiro grupo: '))
nome4 = str(input('Quarto grupo: '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de apresentação das bandas é')
print(lista)

