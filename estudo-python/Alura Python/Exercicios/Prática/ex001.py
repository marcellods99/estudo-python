#1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

valormax = max(num, num2)

print(f'O valor mais alto entre {num} e {num2} é: {valormax}')