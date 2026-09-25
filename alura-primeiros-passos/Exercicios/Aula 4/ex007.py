#7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input('Digite um número: '))

if num <= 1:
    print('Não é primo')
else:
    eh_primo = True
    for divisor in range(2, num):
        if num % divisor == 0:
            eh_primo = False
            break
            
    if eh_primo:
        print('É primo')
    else:
        print('Não é primo')