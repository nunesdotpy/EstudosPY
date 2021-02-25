cash = float(input('Quanto dinheiro você tem na carteira?\nR$'))
dolar = cash / 5.40
print('Com R${:.2f} você pode comprar U${:.2f}'.format(cash, dolar))