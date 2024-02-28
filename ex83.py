valor = str(input('digite uma espressão: '))
lista = []
for sim in valor:
    if sim == '(':
        lista.append('(')
    elif sim == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A sua espressão esta correta')
else:
    print('A sua expressão esta errada')