produto = ('lapis', 1.00,
           'borracha', 0.50,
           'tesooura', 5.00,
           'caderno', 30.00)
print('='*30)
print(f'{"Listagem De Preço":^30}')
print('='*30)
for p in range(0, len(produto)):
    if p % 2 == 0:
        print(f'{produto[p]:.<30}R$', end=' ')
    if p % 2 == 1:
        print(f'{produto[p]:>7.2f}')
print('='*30)
