'''num = list()
for n in range(0, 5):
    v = int(input('Digite um número: '))
    if n == 0 or v > num[-1]:
        num.append(v)
        print('adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(num):
            if v <= num[pos]:
                num.insert(pos, v)
                print(f'o valor foi adicionado na posiçao {pos}')
                break
            pos += 1
print(f'os valore que voce digitou foi {num}')
'''
import bisect

num = []
for c in range(0, 5):
    v = int(input('digite um valor: '))
    bisect.insort(num, v)
    print(f'o valor {v} foi acicionado na posicao {num.index(v)}')
print(f'os valores digitados na sequencias são {num}')