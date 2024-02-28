v = float(input('qual a velocidade do carro?'))
m = (v - 80) * 7.00
if v <= 80:
    print('tenha um bom dia !dirige com segurança!')
else:
    print('MULTADO!VOCÊ TEM QUE PAGAR UMA MULTA DE {:.2f}!'.format(m))

