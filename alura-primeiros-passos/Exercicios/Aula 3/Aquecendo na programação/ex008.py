#8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

num = int(input('Digite um número inteiro: '))


if num % 2:
    print('É impar')
else:
    print('É par')