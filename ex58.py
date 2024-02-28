from random import randint
computador = randint(0, 10)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSera que consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais...tente mais uma vez')
        else:
            print('menos...tente mais uma vez.')
print('Acertou com {} tentativas PARABÉNS !'.format(palpites))
