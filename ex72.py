c = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze',
       'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 à 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {c[num]}')
    else:
        print('tente novamente.')
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(' FIM DO PROGRAMA')