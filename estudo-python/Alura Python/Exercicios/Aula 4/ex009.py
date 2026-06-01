'''
9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).

'''

lista = [1] #jean
lista2 = [2] #jonathan
lista3 = [3] #josé
lista4 = [4] #joyce
lista5 = [5] #nulo

print('[1] - Jean\n[2] - Jonathan\n[3] - José\n[4] - Joyce\n[5] - Nulo ')

while True:
    candidatos = int(input('\n'))
    if candidatos <= 0:
        break

    if candidatos == "1":
        lista
