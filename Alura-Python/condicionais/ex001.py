#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

num = int(input('Digite um número: \n'))
if num % 2 == 0:
    print('O número é par.')
else:
    print('O número é impar.')