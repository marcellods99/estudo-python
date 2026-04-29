#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.


num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

r1 = 'par' if num1 % 2 == 0 else 'ímpar'
r2 = 'par' if num2 % 2 == 0 else 'ímpar'

print('Escolha qual operação você deseja usar:\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão')

op = input('\nEscolha a operação (1-4):')
if op == '1':
    resultado = num1 + num2
elif op == '2':
    resultado = num1 - num2
elif op == '3':
    resultado = num1 * num2
elif op == '4':
    resultado = num1 / num2
else:
    print("banana")

re1 = 'positivo' if num1 > 0 else 'negativo'
res2 = 'positivo' if num2 > 0 else 'negativo'

resp = 'inteiro' if num1 == int(num1) else 'decimal'
respos = 'inteiro' if num2 == int(num2) else 'decimal'


r_res = 'par' if resultado % 2 == 0 else 'ímpar'
re_res = 'positivo' if resultado > 0 else 'negativo'
resp_res = 'inteiro' if resultado == int(resultado) else 'decimal'

print(f'O {num1} é {r1}, {re1} e {resp}\nO {num2} é {r2}, {res2} e {respos}')
print(f'O resultado {resultado} é {r_res}, {re_res} e {resp_res}')