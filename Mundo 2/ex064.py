# tratando e somando valores

num = int(input('Digite um número [999 para parar o processo]: '))
num = cont = soma = 0

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar o processo]: '))

print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))

# assim lendo o flag (999) fora do while ele o desconsidera na somagem


