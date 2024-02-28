somaidade = 0
mediaidade = 0
maiorhomem = 0
nomeelho = ''
totmulher = 0
for c in range(1, 5):
    print('---- {}° PESSOA ----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomeelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomeelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade += somaidade / 4
print('a média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorhomem, nomeelho))
print('Ao todos são {} mulheres com menos de 20 anos.'.format(totmulher))
