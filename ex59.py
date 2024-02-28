from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
num = 1
while num != 5:
    print('-=-' * 20)
    num = int(input('[1] SOMA\n'
                    '[2] MULTIPLICAR\n'
                    '[3] MAIOR\n'
                    '[4] NOVOS NUMEROS\n'
                    '[5] SAIR DO PROGRAMA\n'
                    '>>>>QUAL É A SUA OPÇÃO? '))
    print('-=-' * 20)
    if num == 1:
        soma = n1 + n2
        print('a soma de {} + {} = {}'.format(n1, n2, soma))
    elif num == 2:
        soma = n1 * n2
        print('A multiplicação de {} * {} = {}'.format(n1, n2, soma))
    elif num == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('o maior numero entre {} e {} é {}.'.format(n1, n2, maior))
    elif num == 4:
        print('informe o valor novamente...')
        sleep(1)
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif num == 5:
        print('finalizando...')
        sleep(1)
    else:
        print('\033[33mOpção invalida, tente no novamente...\033[m')
print('progama finalizado volte sempre!')
print('-=-' * 20)
