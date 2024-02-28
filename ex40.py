n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
s = (n1+n2)/2
if s >= 7:
    print('sua media é {} APROVADO'.format(s))
elif s >= 5 < 6.9:
    print('sua media é {} RECUPERAÇÃO.'.format(s))
else:
    print('sua media é {} REPROVADO.'.format(s))
