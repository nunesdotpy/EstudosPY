import math
ang = float(input('Informe o angulo: '))
print('O anglo {:.2f} tem o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))