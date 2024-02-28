numero = list()
while True:
    num = int(input('digite um numero: '))
    if num not in numero:
        numero.append(num)
        print('valor adicionado com sucesso...')
    else:
        print('valor ja adicionado...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
numero.sort()
print(f'Os valores que voce digitou foi {numero}')