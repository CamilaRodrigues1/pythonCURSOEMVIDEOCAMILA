n = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maísculas é {}'.format(n.upper()))
print('Seu nome em minúsculas é {}'.format(n.lower()))
print('Seu numero tem {} letras'.format(len(n) - n.count(' ')))
#print('o seu primeiro nome tem {}'.format(n.find(' '))
separa = n.split()
print('seu primeiro e {} e ele tem {} letras'.format(separa[0], len(separa[0])))