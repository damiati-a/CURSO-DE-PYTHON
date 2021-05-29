# Mostrando a soma de dois números

n1 = int(input('Coloca um número ai: '))
n2 = int(input('Coloca outro ai: '))
s = n1 + n2
print('A soma de {} e {}, deu {}'.format(n1, n2, s))


n3 = int(input('Põe mais um: '))
n4 = int(input('Só mais um: '))
s1 = n3 + n4
print('A soma de {} e {} da {}'.format(n3, n4, s1))

z = s + s1
print('A soma de tudo da {}'.format(z))
