sal = float(input('Qual é o salário do funcionário?\nR$'))
aum = int(input('Qual a porcentagem de aumento?\n> '))
nsal = sal + ((sal * aum) / 100)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(sal, aum, nsal))