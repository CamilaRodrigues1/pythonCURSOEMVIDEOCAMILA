print('{:=^40}'.format('LOJAS CAMILA'))
valor = float(input('digite o valor das suas compras : '))
produto = float(input('''opção de pagamento:
[1] Á VISTA DINHEIRO OU CHEQUE 
[2] Á VISTA NO CARTÃO
[3] EM ATÉ 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO
QUAL É A SUA OPCAO:
'''))
if produto == 1:
    d = valor - (valor * 10 / 100)
elif produto == 2:
    d = valor - (valor * 5 / 100)
elif produto == 3:
    d = valor
    par = valor / 2
    print('sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(par))
elif produto == 4:
    d = valor + (valor * 20 / 100)
    totparcela = int(input('''quantas parcela será :'''))
    parcela = d / totparcela
    print('Sua compra vai ser parcelado em {}X ,cada parcela sai á R${:.2f} COM JUROS'.format(totparcela, parcela))
else:
    d = valor
    print('OPÇÃO INVALIDA TENTE NOVAMENTE!')
print('A sua compras de R${:.2f} vai ficar no valor de R${:.2f}'.format(valor, d))
print('=' * 40)