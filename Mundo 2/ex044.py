# Gerenciador de pagamentos

print('{:=^40}'.format(' LOJAS DAMIATI '))

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTOS
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 } 3X OU MAIS NO CARTÃO''')

opcao = int(input('Qual a opção de pagamento? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao ==2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparc,parcela))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')

print('Sua compra de R$ {} sairá por R$ {}!'.format(preco, total))
