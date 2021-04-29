from random import randint
lista = {"John": 1, "Michael": 2, "Shawn": 3}

list_of_key = list(lista.keys())
list_of_value = list(lista.values())

computador = randint(1, 3)

position = list_of_value.index(computador)
print(list_of_key[position])

position = list_of_value.index(computador)
print(list_of_key[position])