galera = list()
dado = list()
totma = totme = 0
for c in range(0, 4):
    dado.append(str(input('NOME: ')))
    dado.append(int(input('IDADE: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totma += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totme += 1
print(f'temos {totma} maior de idade e {totme} menor de idade.')
for v in galera:
    print(f'{v[0]} tem {v[1]} anos')