lista =('camila', 'aprender', 'cama', 'sofa', 'celular', 'teclado', 'copo', 'caderno',
         'livro', 'televisao', 'lanterna', 'estante')
for lest in lista:
    print(f'\nNa palavra {lest.upper()} tem as vogais ', end='')
    for p in lest:
        if p.lower() in 'aeiou':
            print(p, end=' ')

