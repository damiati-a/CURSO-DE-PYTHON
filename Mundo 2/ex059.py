# Menu matematico

from time import sleep


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior valor
[ 4 ] Novos números
[ 5 ] Sair do programa\n''')
    opcao = int(input('Qual é sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior deles é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números desejados novamente: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('FINALIZANDO...')
        sleep(2)
    else:
        print('OPÇÃO INVÁLIDA. DIGITE NOVAMENTE!')
    print('=+='*10)
print('Obrigado por nos consultar!')
sleep(2)
print('ATENCIOSAMENTE EQUIPE DE NÚMEROS DAMIATI')
