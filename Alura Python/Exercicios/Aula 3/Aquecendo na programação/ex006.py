"""
Questão 6
Escreva um programa que leia três números e os exiba em ordem decrescente.
"""

import statistics

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

maior_valor = max(num1, num2, num3)
medio_valor = statistics.median([num1, num2, num3])
menor_valor = min(num1, num2, num3)

print(f'Maior valor: {maior_valor}, Valor médio: {medio_valor}, Menor Valor: {menor_valor}')