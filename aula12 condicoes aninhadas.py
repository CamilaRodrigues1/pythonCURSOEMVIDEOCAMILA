nome = str(input('Qual é o seu nome? '))
if nome == 'camila' or nome == 'jessy' or nome == 'noah' or nome == 'john':
    print('Que nome lindo você tem!')
elif nome == 'roselia' or nome == 'maria' or nome == 'marcelo':
    print('seu nome é bem popular no brasil. ')
elif nome in 'ana vitoria sarah':
    print('belo nome feminino')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))