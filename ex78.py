num = []
mai = men = 0
for cont in range(0, 5):
    num.append(int(input(f'digite um valor na posição {cont}°: ')))
    if cont == 0:
        mai = men = num[cont]
    else:
        if num[cont] > mai:
            mai = num[cont]
        if num[cont] < men:
            men = num[cont]
print(f'Você digitou os números{num}')
print(f'O maior numero é o {mai} na posiçao ',end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nO menor numero é o {men} na posição ', end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end='')
print()
print('Fim do programa!')
