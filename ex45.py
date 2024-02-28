from random import randint
from time import sleep
import emoji
itens = ('\033[33mpedra\033[m', '\033[32mpapel\033[m', '\033[34mtesoura\033[m')
computador = randint(0,2)
print('''SUAS OPÇÕES:
\033[33m[0]PEDRA\033[m
\033[32m[1]PAPEL\033[m
\033[34m[2]TESOURA\033[m''')
jogador = int(input('qual é sua jogada? '))
print('\033[33mPEDRA\033[m')
sleep(1)
print('\033[32mPAPEL\033[m')
sleep(1)
print('\033[34mTESOURA\033[m!!!')
sleep(2)
print('-=' * 15)
print('o computador escolheu {}'.format(itens[computador]))
print('o jogador jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('\033[31mEMPATE\033[m')
    elif jogador == 1:
        print('\033[35mO JOGADOR GANHOU\033[m')
    elif jogador == 2:
        print('\033[36mO COMPUTADOR GANHOU\033[m')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('\033[36mO COMPUTADOR GANHOU\033[m')
    elif jogador == 1:
        print('\033[31mEMPATE\033[m')
    elif jogador == 2:
        print('\033[35mO JOGADOR GANHOU\033[m')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('\033[35mO JOGADOR GANHOU\033[m!')
    elif jogador == 1:
         print('\033[36mO COMPUTADOR GANHOU\033[m!')
    elif jogador == 2:
        print('\033[31mEMPATE!\033[m')
    else:
        print('JOGADA INVALIDA!')

print('-=' * 15)
