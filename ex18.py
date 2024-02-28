from math import radians,sin, cos, tan
an = int(input('Digite o angulo que voce deseja: '))
ra = radians(an)
se = sin(ra)
co = cos(ra)
ta = tan(ra)
print('O angulo de {:.2f} tem o SENO de {:.2f} '.format(an,se))
print('O ãngulo de {:.2f} tem o COSSENO de {:.2f} '.format(an,co))
print('O ãngulo de {:.2f} tem a TANGENTE de {:.2f}'.format(an,ta))