"""
Questão 5
Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
"""

n1 = int(input('Digite um número: '))
denominador = int(input('Digite o denominador: '))
if denominador == 0:
  print(f'Erro: A divisão não pode ser zero!')
else:
  divisao = n1 / denominador
  print(f'A divisão de {n1} e {denominador} é igual a {divisao:.2f} ')