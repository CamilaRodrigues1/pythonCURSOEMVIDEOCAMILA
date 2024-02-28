num = []
while True:
    numero = int(input('Digite um número: '))
    num.append(numero)
    resp = ''
    resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'A lista de numeros é {num}')
print('Os números pares sao ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
print('\nOs números impares sao ', end='')
for n in num:
    if n % 2 == 1:
        print(f'{n}', end=' ')
