# Verificando as primeiras linhas de um texto, dizendo se a cidade começa ou não  com SANTO

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[0:5].upper() == 'SANTO') # jogando tudo para maiusculo, não se corre risco de dar errado



