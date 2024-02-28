"""import random
print('-' * 20)
print("vou pensar em um numero de 0 á 5.Tente adivinhar...")
print('-' * 20)
n = int(input('em que numero eu estava pensando?'))
num = random.randint(0, 5)
if n == num:
    print('parabens voce ganhou'.format(n))
else:
    print('eu ganhei estava pensando no {} e nao no {}'.format(num, n))"""


from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'* 20)
print('vou pensar em um numero de 0 á 5 e tente adivinhar!!')
print('-=-'* 20)
jogador = int(input('em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS!você ganhou!!')
else:
    print('eu ganhei!Estava pensando no {} e nao no {}'.format(computador,jogador))
