num = int(input('Digite um número inteiro: '))
print('''ESCOLHA UMA DAS BASES PARA CONVERTER:
[1]BINARIO
[2]OCTAL
[3]HEXADECIMAL
[4]PARA CONVERTAR PARA OS 3 OPÇAÃO ACIMA''')
op = int(input('escolha a sua opção: '))
if op == 1:
    print('{} convertido pra binario é {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido em octal  é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido pra hexal é igual a {}.'.format(num, hex(num)[2:]))
elif op == 4:
    print('{} convertido para binario é igual {}, para octal é igual a {}, hexal é de {}'.format(num, bin(num)[2:], oct(num)[2:], hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA')
