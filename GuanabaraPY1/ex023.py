''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4 dezena: 3 centena: 8 milhar: 1
'''
num = int(input('Informe um número: '))
'''n = str(num)
print('Analisando o número: {}'.format(num))
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(n[3],n[2],n[1],n[0]))
''' # Uma das formas de se trabalhar com isso
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u,d,c,m))