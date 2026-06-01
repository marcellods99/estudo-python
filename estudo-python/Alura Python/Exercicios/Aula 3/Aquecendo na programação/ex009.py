#9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

num = float(input('Digite um número: '))

if num == int(num):
    print('inteiro')
else:
    print('Decimal')