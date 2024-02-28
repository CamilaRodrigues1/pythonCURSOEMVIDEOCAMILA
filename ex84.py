pessoa = []
dados = []
maior = menor = total = 0
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    if len(pessoa) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    resp = ''
    resp = str(input('Quer continuar?[S/N]')).strip().upper()
    if resp == 'N':
        break
print(f'foram cadastrado {len(pessoa)} pessoas.')
print(f'O maior peso é de {maior:.2f} kg', end='')
for p in pessoa:
    if p[1] == maior:
        print(f' de {p[0]}', end='')
print(f'\nO menor peso é {menor:.2f} kg', end='')
for p in pessoa:
    if p[1] == menor:
        print(f' de {p[0]}', end='')
