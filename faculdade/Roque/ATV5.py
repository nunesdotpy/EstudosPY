import random
import operator

class Processo(object):

#construtor
    def __init__(self, nome, burst, tcheg): #self é igual ao this em Java
        self.nome = nome
        self.burst = burst
        self.tcheg = tcheg

    def setNome(nome):
        self.nome = nome

    def setBurst(burst):
        self.burst = burst

    def setTcheg(tcheg):
        self.tcheg = tcheg

n = int(input('Qual a quantidade de processos?'))
lista = []

c = str(input('Burst manual ou aleatório(M/A)?'))

#n é uma variavel
n = int(input('Qual a quantidade de processos?'))
lista = [] #isso é uma lista, que chamamos de vetor tb

c = input('Burst manual ou aleatório(M/A)?')

if c == 'A':
    #burst é tempo de chegada automático
    for i in range(n):
        proc = Processo(i, random.randint(1,100), random.randint(0, 15))
        lista.append(proc) #append é adicionar
else:
    #burst é tempo de cehgada manual
    for i in range(n):
        b = int(input("P" + str(i) + " Burst:"))
        t = int(input("P" + str(i) + " Tempo de Chegada:"))
        proc = Processo(i,b,t)
        list.append(proc)

print("Todos os processos...")
print("proc","burst","tcheg")

for i in list:
    print(i.nome," ",i.burst," ",i.tcheg)

#ordenando os objetos pelo burst
print(" ")
print("Objetos ordenados pelo burst")
lista.sort(key=operator.attrgetter("burst"),reverse=False)
print("proc","burst",)
for i in list:
    print(i.nome," ", i.burst)

#ordenando os objetos pelo tempo de chegada
print(" ")
print("Objetos ordenados pelo tempo de chegada")
lista.sort(key=operator.attrgetter("tcheg"),reverse=False)
print("proc","burst","tcheg")
for i in lista:
    print(i.nome," ", i.burst," ", i.tcheg)