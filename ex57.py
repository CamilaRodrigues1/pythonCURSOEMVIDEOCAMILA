s = str(input('qual é o seu sexo ? [M/F]')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('dados invalidos.Por favor, informe seu sexo :[M/F]')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(s))
