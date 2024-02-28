f = str(input('digite uma frase: ')).upper().strip()
print('A letra A apareceu {} vezes na frase'.format(f.upper().count('A')))
print('A primeira letra A apareceu na posição {} '.format(f.find('A')+1))
print('A  última letra A apareceu na posição {} '.format(f.rfind('A')+1))