# Manipulação de textos


# Fatiamento ->
frase = str(input('frase: '))
print(frase[0:16:2])

'''
com :2 ela vai indicar que termine no bloco 2.
com 2: indica para fatiar até o final da string
com 2::2, vai começar no 2 e vai até o final pulando de 2 em 2.

'''

# Análise de string
print(len(frase))  # te mostra a quantidade de caracteres na frase
print(frase.count('o'))  # te mostra a quantidade de letras 'o' na frase
print(frase.find('deo'))
print(frase.find('Android'))  # quando não tem uma string solicitada, o python retorna com -1


# Transformação
frase.replace('credo', 'gostoso')  # Substitui as palavras
frase.upper()  # deixa tudo em maiusculo
frase.lower()  # deixa tudo em minusculo
frase.title()  # deixa somente as primeiras letras em maiusculas
frase.capitalize()  # somente o primeiro caractere fica maiusculo
frase.rstrip()  # remove os espaços da direita
frase.lstrip()  # remove os espaços da esquerda
frase.strip()  # remove todos os espaços


# Divisão
frase.split()  # Separa cada palavra em uma lista

# Junção
'_'.join(frase)  # juntando as palavras separadas por um '-'

##############################
frase = 'curso em video python'
print(frase[1::2])

# para imprimir texto todo utilizar """ texto """

print(frase.replace('python', 'gertrude'))

print(frase.split())
dividido = frase.split()
print(dividido[2][3])


