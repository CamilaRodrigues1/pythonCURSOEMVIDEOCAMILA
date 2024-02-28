lanche = 'hambúrguer', 'suco', 'pizza', 'pudim', 'batata-frita'
#PRA COLOCAR EM ORDEM ALFABETICA
print(sorted(lanche))
print(lanche)
#se eu nao precisar da posiçao
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('=='*30)
#seu eu precisar da posiçao
for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
print('=-'*30)
for pos, comida in enumerate(lanche):
    print(F'Eu vou comer {comida} na posição {pos}')
print('=-'*30)
print('Comi pra caramba')
