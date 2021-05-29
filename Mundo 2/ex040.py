# Média de um aluno

pnota = float(input('Digite a primeira nota do aluno: '))
snota = float(input('Digite a segunda nota do aluno: '))

media = (pnota + snota) / 2
print('A sua média final foi de {}'.format(media))

if media > 7:
    print('PARABÉNS! Você terminou o semestre com média {} e está aprovado!'.format(media))
elif media < 7 > 5:
    print('Infelizmente você terminou com média {} e precisará fazer uma RECUPERAÇÃO!.'.format(media))
else:
    print('Você está REPROVADO! terá de refazer este semestre, pois sua média foi de {} e está abaixo do necessário'.format(media))

print('NUNCA DEIXEM DE ESTUDAR!')