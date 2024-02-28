from datetime import date
atual = date.today().year
cont = 0
con = 0
for pessoas in range(1, 8):
    data = int(input('digite a data de nascimento de {}°: '.format(pessoas)))
    idade = atual - data
    if idade >= 18:
        cont += 1
    else:
        con += 1
print('são {} pessoas maiores de idade'.format(cont))
print('são {} pessoas menores de idade'.format(con))
