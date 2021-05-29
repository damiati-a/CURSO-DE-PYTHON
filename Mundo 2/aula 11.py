# Interrompendo repetições em while

"""
enquanto Verdaddeiro
    se terra
        passo
    se vazio
        pula
    se moeda
        pega
    se trofeu
        pula
        interrompa
pega

"""
"""
while True:
    if terra:
        passo
    if vazio:
        pula
    if moeda:
        pega
    if trofeu:
        pula
        break
pega
"""
"""
cont = 1
while cont <= 10:
    print(cont)
    cont += 1
print('fim')
"""
n = s = 0
while True:
    n = int(input('Um número: '))
    if n == 999:
        break  # ele sai do looping infinito
    s += n
# print('A soma de tudo vale {}'.format(s))
print(f'A soma de tudo vale {s}')  # f string


