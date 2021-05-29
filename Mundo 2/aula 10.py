# Estruturas de repetição while

# a estrutura FOR é utilizada apenas quando se sabe o limite, quando não se sabe a quantidade usa-se o WHILE
"""
enquanto não (maça)
    passo
pega (maça)

while not(maça):
    passo
pega

"""
"""
enquanto não(maça):
    se (chão):
        passo
    se (buraco):
        pula
    se (moeda):
        pega
pega

"""
"""
while not(maça):
    if (chão):
        passo
    if (buraco):
        pula
    if (moeda):
        pega
pega

"""
"""
for c in range(1, 10):
    print(c)
    
c = 1
while c < 10:
    print(c)
    c += 1
"""
# while e for são estruturas de repetição para situações diferentes
"""
n = 1
while n != 0:
    n = int(input('Um valor: '))
print('fim')
"""
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('voce digitou {} números pares e {} números impares'.format(par, impar))
