# Escreva  um programa que pergunte a distância que um passageiro deseja percorrer em km. Em seguida, calcule o preço da passagem, cobrando R$0,55 por km para viagens de  até 100km, R$0,50 por km para  viagens de até 200km, e R$0,45 por km para  viagens mais longas.

dist = int(input('Qual a distância que deseja percorrer?\n> '))
if dist <= 100:
    price = dist * 0.55
elif dist <= 200:
    price = dist * 0.50
else:
    price = dist * 0.45
print('Com a sua viagem de {}km você deve pagar R${:.2f}'.format(dist, price))