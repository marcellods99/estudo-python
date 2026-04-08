"""
Questão 8
Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
"""

n1 = int(input('Digite um número: '))
denominador = int(input('Digite outro número: '))

if denominador == 0:
    print('Erro: O denominador não pode ser 0.')
else:
    rdiv = n1 // denominador
    print(f'A divisão inteira de {n1} por {denominador} é {rdiv}!')