# Detector de Palíndromo

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# ou 'inverso = junto[::-1]'  # ai não precisaria utilizar o for abaixo.
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase não forma um Palíndromo!')



