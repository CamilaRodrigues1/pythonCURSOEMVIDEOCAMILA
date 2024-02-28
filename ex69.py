maior = homem = mulher = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('SEXO: [F/M]')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulher += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('quer continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
            break
print(f'pessoas maiores de 18 anos : {maior}')
print(f'foram cadastrado {homem} homens.')
print(f'foram cadastrada {mulher} mulheres.')
