#2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

colo_a = 4
colo_b = 10
dias = 0

while colo_a < colo_b:
    colo_a *= 1.03
    colo_b *= 1.015
    dias += 1

print(f"Dias necessários: {dias}")
print(f"Final - Colônia A: {colo_a:.2f}")
print(f"Final - Colônia B: {colo_b:.2f}")