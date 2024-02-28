menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso é o {}kg'.format(maior))
print('o menor peso é o {}kg'.format(menor))

