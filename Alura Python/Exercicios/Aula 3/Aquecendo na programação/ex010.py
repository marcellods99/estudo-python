#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 % 2:
    print('É impar')
    if num2 % 2:
        print('É impar')
else:
    print('É Par')