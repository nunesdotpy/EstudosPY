dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${}'.format(total))