num = int(input('''Digite um numero para
calcular o seu fatorial: '''))
con = num
f = 1
print('calculando fatorial de {}! = '.format(num), end='')
while con > 0:
    print('{}'.format(con), end='')
    print(' x 'if con > 1 else ' = ', end='')
    f *= con
    con -= 1
print(' {}'.format(f))
