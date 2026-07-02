from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(100))


print(sample(lista, 5))