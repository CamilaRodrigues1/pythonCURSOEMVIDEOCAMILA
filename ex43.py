p = float(input('digite seu peso : '))
a = float(input('digite a sua altura: '))
imc = p / (a ** 2)
print('voce esta com imc de {:.2f}'.format(imc), end=' ')
if imc < 18.5:
    print('MUITO ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
