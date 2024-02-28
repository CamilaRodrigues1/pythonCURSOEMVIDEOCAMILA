print('-'*30)
print('{:^30}'.format('BANCO CM'))
print(' -'*30)
sacar = int(input('quanto voce quer sacar? R$ '))
total = sacar
ced = 100
totalcel = 0
while True:
    if total >= ced:
        total -= ced
        totalcel += 1
    else:
        if totalcel > 0:
            print(f'Total de {totalcel} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalcel = 0
        if total == 0:
            break
print('-='*30)
print('Volte sempre ao BANCO CM! '
      'TENHA UM BOM DIA')
