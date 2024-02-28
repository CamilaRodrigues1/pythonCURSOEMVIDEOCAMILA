
continuar = 'S'
cont = media = maior = menor = soma =0
while continuar in 'Ss':
    num = int(input('digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    continuar = str(input('quer continuar? [s/n]')).strip().upper()[0]
media = soma / cont
print('Você digitou {} números e a sua media é {:.2f}'.format(cont, media))
print('o maior numero é {} e o menor é {}'.format(maior, menor))