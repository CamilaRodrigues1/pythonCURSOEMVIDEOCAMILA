t1 = float(input('primeiro segmento:'))
t2 = float(input('segundo segemnto: '))
t3 = float(input('terceiro segmento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('os segmento acima formam um triangulo ', end='')
    if t1 == t2 == t3:
        print('EQUILÁTERO')
    elif t1 != t2 != t3 != t1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('os segmento acima nao PODEM forma um triangulo.')
