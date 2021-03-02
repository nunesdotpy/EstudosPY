nome = str(input('Digite seu nome completo: '))
pnome = nome.split()
'''ipnome = nome.strip().rfind(' ') + 1
unome = nome[ipnome::]''' # feita by nunesdotpy
print('Prazer em te conhecer! \nSeu primeiro nome é {}'.format(pnome[0]))
print('Seu ultimo nome é {}'.format(pnome[len(pnome)-1]))