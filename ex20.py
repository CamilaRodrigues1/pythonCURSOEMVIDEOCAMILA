'''from random import choices
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto  aluno: '))
lista = [n1,n2,n3,n4]
sorteado = choices(lista)
print('a ordem de apresentacao sera :')
print("['{}', '{}', '{}', '{}']".format(sorteado,sorteado,sorteado,sorteado))'''

'''import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto  aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('a ordem de apresentaçao sera: ')
print(lista)'''


from random import shuffle
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto  aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('a ordem de apresentaçao sera: ')
print(lista)