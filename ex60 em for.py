num = int(input('digite um valor para calcular o seu fatorial: '))
con = num
f = 1
print('calculando {}! = '.format(num), end='')
for con in range(num, 0, -1):
    print('{}'.format(con), end='')
    print(' x 'if con > 1 else ' = ', end='')
    f *= con
print('{}'.format(f), end='')
