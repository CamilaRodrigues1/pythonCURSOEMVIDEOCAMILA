num = int(input('digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[35m{}'.format(c), end=' ')
        tot += 1
    else:
        print('\033[33m{}\033[m'.format(c), end=' ')
if tot == 2:
    print('o numero {} é PRIMO'.format(num))
else:
    print('O número {} não é PRIMO'.format(num))
