numero = []
#cont = 0
while True:
    num = int(input('digite um valor: '))
    numero.append(num)
    #cont += 1
    resp = ''
    resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
if 5 in numero:
    print(f'o numero 5 foi adicionado na lista')
else:
    print('o numero 5 nao foi adicionado')
print(f'Foram digitados {len(numero)} números.')
numero.sort(reverse=True)
print(f'Os números na ordem decrescente {numero}')
