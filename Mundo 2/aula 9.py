# Estruturas de repetição (for)

'''
faço 'c' no intervalo(1,10)
for 'c' in range(1,10)
'''
'''
laço c no intervalo(0,3)
    passo
    pula
passo
pega
#################################
for c in range(0,3)
    passo
    pula
passo
pega
'''

'''
for c in range(0,3)
    if moeda:
        pega
    passo
    pula
passo
pega
'''

# Parte Parática
'''
for c in range(0, 30, 3):
    print(c)
print('FIM')
'''
'''
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')
'''
'''
i = int(input('Inicio: '))  # qual numero começar
f = int(input('Fim: '))  # qual numero terminar
p = int(input('Passo: '))  # e de quanto em quanto pular
for c in range(i, f + 1, p):
    print(c)
print('fim')
'''

for c in range(0, 3):
    n = int(input('DIgite um numero: '))  # vai solicitar que se digite um numero 3 vezes
    s = n + n
print('O somatorio de tudo foi: {}'.format(s))
