from random import randint
from time import sleep
print('=-'*20)
print('PAR OU IMPAR')
print('-='*20)
ganhei = 0
while True:
    jogador = int(input('digite um valor:'))
    computador = randint(1, 10)
    soma = computador + jogador
    escolha = ' '
    while escolha not in 'IP':
        escolha = str(input('par ou impar? [I/P]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador} o seu total é {soma}', end=' ')
    print('deu PAR'if soma % 2 == 0else 'deu IMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você GANHOU!')
            ganhei += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você GANHOU!')
            ganhei += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break
    print('vamos jogar NOVAMENTE....')
    sleep(1)
print(f'\033[31mGAME OVER!\033[m\nVocê ganhou {ganhei} vezes.')
