"""
Questão 4
Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
"""

valor2024 = 204000
valor2025 = 266000
valor2026 = 265000

maior_valor = max(valor2024, valor2025, valor2026)
menor_valor = min(valor2024, valor2025, valor2026)

print(f'O valor mais alto é: R$ {maior_valor:,.2f}')
print(f'O valor mais baixo é: R$ {menor_valor:,.2f}')
