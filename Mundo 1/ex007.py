# Ordem aritmética

n1 = float(input('Nota do primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
m = (n1 + n2) / 2    # () para ordem de precedencia
print('A média entre {:.1f} e {:.1f} é de: {:.1f} '.format(n1, n2, m))

# :.1f = significa que usará apenas um ponto após a virgula (0.05 = 0.5)
