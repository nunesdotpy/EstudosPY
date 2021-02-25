tempc = float(input('Informe a temperatura em ºC: '))
tempf = (tempc * 9 + 160) / 5
tempk = tempc + 273
print('A temperatura de {}ºC corresponde a {}ºF e {} K'.format(tempc, tempf, tempk))