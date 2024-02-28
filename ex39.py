from datetime import date
sexo = int(input('''qual é o seu sexo:
[1]masculino 
[2]feminino 
escolha a sua opção:'''))
if sexo == 1:
    a = date.today().year
    nas = int(input('digite a seu ano de nascimento: '))
    i = a - nas
    print('quem nasceu em {} tem {} em {}'.format(nas, i, a))
    if i == 18:
        print('voce tem que se alista imediatamente!')
    elif i < 18:
        saldo = 18 - i
        print('falta {} anos para voce se alistar'.format(saldo))
        ano = saldo + a
        print('o seu ano de alistamento será em {}.'.format(ano))
    elif i > 18:
        saldo = i - 18
        print('voce ja deveria ter se alistado há {} anos'.format(saldo))
        ano = a - saldo
        print('seu ano de alistamento foi em {}'.format(ano))
elif sexo == 2:
    print('voce é mulher nao é obrigatorio se alistar')
