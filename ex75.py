a = (int(input('DIGITE UM VALOR: ')),
    int(input('DIGITE SEGUNDO VALOR: ')),
    int(input('DIGITE TERCEIRO VALOR: ')),
    int(input('DIGITE QUARTO VALOR: ')))
print(f'Voce digitou {a}')
if 9 in a:
    print(f'Você digitou o valor (9), {a.count(9)} vezes')
else:
    print('o valor 9 nao foi digitado')
if 3 in a:
    print(f'O número 3 foi digitado na {a.index(3)+1}° posição.')
else:
    print('O número 3 não apareceu em nenhuma posição.')
cont = 0
print(f'Os números pares são:',end='')
for n in a:
    if n % 2 == 0:
        cont += 1
        print(f'{n}', end=' ')
print(f'\nForam digitados {cont} valores pares')

