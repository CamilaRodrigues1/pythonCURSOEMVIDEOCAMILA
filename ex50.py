cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite {}° número: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('A soma dos {} valores pares são {}'.format(cont, soma))
