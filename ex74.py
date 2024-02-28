from random import randint
n = (randint(0, 20), randint(0, 20), randint(0, 10),
     randint(0, 30), randint(0, 30),)
print(f'os numeros sorteados são: ', end='')
for numeros in n:
    print(f'{numeros}', end=' ')
print(f'\nO maior valor foi: {max(n)}')
print(f'O menor número foi: {min(n)}')
