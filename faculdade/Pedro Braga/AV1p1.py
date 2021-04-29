from random import randint
lista = { 'pedra': 0,
  'spok': 1,
  'papel': 2,
  'lagarto': 3,
  'tesoura': 4}
print('''Opções válidas são:
Pedra
papel
tesoura
lagarto
Spock''')
list_of_key = list(lista.keys())
list_of_value = list(lista.values())

def jogar():
    while True:
        jogador = str(input('\nQual sua jogada?\n> ')).lower()
        if jogador in lista:
            break

    computador = randint(0, 4)
    position = list_of_value.index(computador)
    print('\nO usuário escolheu {}\nComputador escolheu {}'.format(jogador, list_of_key[position]))
    res = (lista[jogador] - computador)%5
    if res == 1 or res == 2:
        print('Computador ganhou!')
    elif res == 3 or res == 4:
        print('Usuário ganhou')
    else:
        print('Usuário e computador empataram')

while True:
    jogar()
    c = str(input('\nContinuar jogando? (Y/N)')).lower()
    if c != 'y':
        print('\nAté a próxima :)')
        break

