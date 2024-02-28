km = float(input('quantos km é a sua viagem? '))
if km <= 200:
    rf = km * 0.50
    print('a sua viagem vai custar {:.2f}'.format(rf))
else:
    rf = km * 0.45
    print('a sua viagem vai custra {:.2f}'.format(rf))
