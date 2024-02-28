"""nome = str(input('Qual é o seu nome? '))
if nome== 'camila':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m>= 6.0:
    print('PARABÉNS')
else:
    print('ESTUDE MAIS')"""

n1 = float(input('DIGITE PRIMEIRA NOTA:'))
n2 = float(input('DIGITE SEGUNDA NOTA:'))
m =(n1+n2)/2
print('a sua media foi {:.1f}'.format(m))
print('PARABENS'if m>= 6.0 else 'ESTUDE MAIS')