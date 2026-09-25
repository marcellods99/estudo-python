"""
Questão 1
Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))


if num1 > num2:
  print(f'O maior número é: {num1}')
elif num2 > num1:
  print(f'O maior número é: {num2}')
else:
  print('Não existe número maior.')