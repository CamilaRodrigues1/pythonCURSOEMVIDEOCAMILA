vcasa = int(input('Qual é o valor da casa: '))
salario = float(input('Qual é o seu salario mensal? '))
anos = int(input('Quantos anos deseja pagar? '))
presraao = vcasa / (anos*12)
soma = salario*30/100
print(f'Uma casa de {vcasa} parcelada em {anos}x vai ter uma prestação de R${presraao:.2f}.')
if presraao <= soma:
    print(f'O seu financiamento foi aprovado!')
else:
    print(f'O seu financiamento foi negado!')
print('fim do programa')
