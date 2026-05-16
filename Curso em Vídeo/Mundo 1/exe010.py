#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Quanto de dinheiro você tem? '))

dolar = 5.06
poder = carteira / dolar

print(f'Com R${carteira} você pode comprar U$ {poder:.2f}.')