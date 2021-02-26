import math
cato = int(input('Qual o comprimento do cateto oposto? '))
cata = int(input('Qual o comprimento do cateto adjacente? '))
h = (cato**2 + cata**2) ** 0.5
print('A hipotenusa é igual a {:.2f}'.format(h))