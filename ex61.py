print('=-=-' * 10)
print('Gerador de PA')
print('=-=-' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
totaldetermo = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    print('=-=-' * 10)
    mais = int(input('quantos termos voce quer ver mais? '))
print('progressão finalizado com {} termos mostrado'.format(total))
print('FIM')
