nomes = ('Palmeiras', 'Botafogo', 'Flamengo', 'Grêmio', 'Red Bull Bragantino', 'Atlético-MG', 'Athletico',
         'Fluminense', 'Cuiabá', 'São Paulo', 'Fortaleza', 'Corinthians', 'Internacional', 'Santos',
         'Vasco', 'Cruzeiro', 'Bahia', 'Goiás', 'Coritiba', 'América-MG')
print(f'A lista do 20° colocados do campeonato Brasileiro:{nomes}')
print('=-'*30)
print(f'O 5 PRIMEIROS TIMES COLOCADOS SÃO :{nomes[:5]}')
print('-='*30)
print(f'OS 4 ULTIMOS TIMES COLOCADOS SÃO :{nomes[-4:]}')
print('-='*30)
print('OS TIMES EM ORDEM ALFABETICAS :')
print(sorted(nomes))
print('-='*30)
print(f'O time da Chapecoense esta na {nomes.index("chapeconse")}° posiçao ')

