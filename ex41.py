from datetime import date
atual = date.today().year
nasc = int(input('Qual é o ano de nascimento do atleta? '))
idade = atual - nasc
if idade <= 9:
    print('O atleta tem {} anos e ele é MIRIN.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e ele é INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta te {} anos e ele é JÚNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e ele é SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e ele é MASTER.'.format(idade))
