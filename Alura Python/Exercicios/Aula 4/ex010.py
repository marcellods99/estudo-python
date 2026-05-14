#6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:


num = int(input('Digite a tabuada: '))

for c in range(1,11):
    print(f'{num} x {c} = {num * c}')