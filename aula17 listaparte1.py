lista = [1, 3, 2, 7]
lista[3] = 3
lista.append(8)
#lista.sort()
lista.insert(2, 9)
lista.sort(reverse=True)
lista.pop()
if 6 in lista:
    lista.remove(6)
else:
    print('nao achei na lista o numero 6')
print(lista)
print(f'essa lista tem {len(lista)} elementos.')