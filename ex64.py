cont = 0
total = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    total += num
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
print('voce digitou {} números e a soma entre eles é {}'.format(cont, total))
