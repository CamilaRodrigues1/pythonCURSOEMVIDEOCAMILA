print('-=-'* 20)
print('\033[31mANALISADOR DE TRIÂNGULOS\033[m')
print('-=-' * 20)
t1 = float(input('primeiro segmento: '))
t2 = float(input('segundo segmento: '))
t3 = float(input('terceiro segmento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('\033[1;35;46mos segmentos acima podem formar um triângulo\033[m!')
else:
    print('\033[1;33;46mos segmentos não podem formar um triângulo\033[m!')
