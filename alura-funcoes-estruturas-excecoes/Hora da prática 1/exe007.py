#7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

from random import randrange

nome = str(input('Digite o seu nome: '))

token = randrange(1000, 10000, 2)

msg = (f'Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!')

print(msg)