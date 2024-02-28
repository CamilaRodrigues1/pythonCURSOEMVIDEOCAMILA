'''c = 'S'
num = 1
while c == 'S':
    num = int(input('digite um numero: '))
    c = str(input('quer continuar? [S/N]')).upper()
print('acabou!')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('voce digitou {} numeros pares e {} numeros impares'.format(par, impar))
