from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(100)) #append adiciona na lista e o randrange pega os números dentro dessa lista


print(sample(lista, 5)) #sample pega 5 números aleatórios da lista