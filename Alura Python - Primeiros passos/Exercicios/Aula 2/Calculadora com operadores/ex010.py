"""
Questão 10
Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
"""

#FeitoporIA

# Valores
n1, n2, n3, n4 = 5, 12, 20, 15

# Pesos
p1, p2, p3, p4 = 1, 2, 3, 4

# Cálculo da média ponderada
# Somamos as multiplicações e dividimos pela soma dos pesos (1+2+3+4 = 10)
soma_ponderada = (n1 * p1) + (n2 * p2) + (n3 * p3) + (n4 * p4)
soma_pesos = p1 + p2 + p3 + p4

media_ponderada = soma_ponderada / soma_pesos

print(f"A média ponderada é: {media_ponderada}")