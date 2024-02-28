'''frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(frase, inverso))
if inverso == frase:
    print('Ele é um PALÍNDROMO')
else:
    print('A frase não é um PALÍNDROMO')'''


frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('o inverso de {} é {}'.format(frase, inverso))
if inverso == frase:
    print('Ele é um PALÍNDROMO')
else:
    print('A frase não é um PALÍNDROMO')
