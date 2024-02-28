t = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(t, c, (c*t)))
print('FIM')
