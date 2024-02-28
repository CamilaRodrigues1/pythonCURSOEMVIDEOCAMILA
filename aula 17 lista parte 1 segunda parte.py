'''valores = []
valores.append(4)
valores.append(5)
valores.append(9)
valores.append(7)'''
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
valores.sort()
for pos, v in enumerate(valores):
    print(f'na posição {pos} tem o numero {v}')
print('acabei o programa')