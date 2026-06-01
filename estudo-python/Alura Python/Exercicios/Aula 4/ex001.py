#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

inicio = min(num1, num2)
final = max(num1, num2)
for c in range(inicio, final + 1):
   print(c)