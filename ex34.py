s = float(input('Qual é o seu sálario atual? '))
if s <= 1250:
    novo = s + (s * 15/100)
else:
    novo = s + (s * 10/100)
print('quem recebe R$ {:.2f} passara a receber R${:.2f}'.format(s,novo))
