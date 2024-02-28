cont = valortot = menor = barato = totmil = 0
while True:
    produto = str(input('nome do produto: ')).strip().upper()
    preco = float(input('preço do produto:R$ '))
    continuar = ' '
    cont += 1
    while continuar not in 'SN':
        continuar = str(input('quer continua?[S/N]')).strip().upper()[0]
    valortot += preco
    if preco >= 1000:
        totmil += 1
    #if cont == 1 or preco < menor: pra nao precisar do else
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if continuar == 'N':
        break
print(f'Sua compra deu um total de R${valortot:.2f}.')
print(f'{totmil} produtos que custa acima de R$1000.00')
print(f'E o produto mais barato {barato} que custa R${menor:.2f}.')
