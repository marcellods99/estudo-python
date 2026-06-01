"""
Questão 5
Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
"""

bolsa1 = int(input('Digite um número: '))
bolsa2 = int(input('Digite mais um número: '))
bolsa3 = int(input('Digite mais um número: '))

maior_valor = max(bolsa1, bolsa2, bolsa3)
menor_valor = min(bolsa1, bolsa2, bolsa3)

print(f'O valor mais alto é: R$ {maior_valor:,.2f}')
print(f'O valor mais baixo é: R$ {menor_valor:,.2f}')