from random import randint
lista = { 'pedra': 0,
  'spok': 1,
  'papel': 2,
  'lagarto': 3,
  'tesoura': 4}
print('''Opções válidas são:
pedra
papel
tesoura
lagarto
spok''')
list_of_key = list(lista.keys()) # Descobrir as keys na lista
list_of_value = list(lista.values()) # Descobrir os values na lista

def jogar():
    while True: # loop para aceitar apenas jogadas validas
        jogador = str(input('\nQual sua jogada?\n> ')).lower()
        if jogador in lista:
            break
    computador = randint(0, 4) # sortear jogada do computador
    position = list_of_value.index(computador) # identificar o número sorteado como jogada
    print('\nO usuário escolheu {}\nComputador escolheu {}'.format(jogador, list_of_key[position]))
    res = (lista[jogador] - computador)%5 # calcular quem ganhou
    if res == 1 or res == 2:
        print('Computador ganhou!')
    elif res == 3 or res == 4:
        print('Usuário ganhou')
    else:
        print('Usuário e computador empataram')

while True: # Loop para saber se o usuário quer jogar novamente
    jogar()
    c = str(input('\nContinuar jogando? (Y/N)')).lower()
    if c != 'y':
        print('\nAté a próxima :)')
        break

