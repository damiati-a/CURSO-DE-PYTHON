# Ler números inteiros e só para quando ler 999, somando e quantos números foram digitados sem o flag(999).

num = contagem = soma = 0

while True:
    num = int(input('Digite um número [999 para encerrar o processo]:  '))

    if num == 999:
        break
    soma += num
    contagem += 1

print(f'Foram digitados {contagem} números e soma de todos é de {soma}')

