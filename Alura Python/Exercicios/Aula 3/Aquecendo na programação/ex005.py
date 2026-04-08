"""
Questão 5
Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
"""

bolsa1 = 200
bolsa2 = 300
bolsa3 = 250

maior_valor = max(bolsa1, bolsa2, bolsa3)
menor_valor = min(bolsa1, bolsa2, bolsa3)

print(f'O valor mais alto é: R$ {maior_valor:,.2f}')
print(f'O valor mais baixo é: R$ {menor_valor:,.2f}')
