# Analisando se o Ano é Bissexto

from datetime import date   # importa datas, anos

ano = int(input('Coloque um ano para ser analisado: '))
if ano == 0:
    ano = date.today().year   # Pega o ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))
