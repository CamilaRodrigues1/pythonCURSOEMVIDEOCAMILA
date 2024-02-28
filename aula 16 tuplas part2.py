'''a = (1, 2, 3, 6, 8)
b = (4, 5, 6)
c = a + b
#pra ficar em ondem numericas
print(sorted(c))
#pra ler quantas numero tem ao todo
print(len(c))
#pra contar quantas vezes aparece no (6) indicado
print(c.count(6))
#em que posiçao esta o numero informado (8)
print(c)
print(c.index(8))
# se tiver mais de um numero no index ele vai contar sempre a primeira aparecer se quiser o outro que tirar ate aonde o primeiro ta ()
#ex
print(c)
print(c.index(6, 3))
print(c.index(6, 4))
'''

pessoa = 'camila', 30, 'F', 90
#se eu quiser apagar da memoria
for p in pessoa:
    print(p,end='.....................R$')
