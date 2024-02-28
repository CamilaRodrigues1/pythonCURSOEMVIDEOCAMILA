while True:
    tabuada = int(input('qual a tabuada que voce quer ver? '))
    if tabuada < 0:
        break
    print('-' * 40)
    for cont in range(1, 11):
        print(f'{tabuada} x {cont} = {tabuada * cont}')
    print('-'*40)
print('PROGRAMA ENCERRADO. Volte sempre')
