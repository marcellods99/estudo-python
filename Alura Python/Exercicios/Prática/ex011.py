#2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

empresa = [2172.54 , 3701.35 , 3518.08 , 3426.61 , 3249.38 , 2840.82 , 2840.82 , 3891.45 , 3075.26 , 2317.64 , 3219.08]

compras3000 = 0

for gasto in empresa:
    if gasto > 3000:
        compras3000 = compras3000 + 1

total_compras = len(empresa)
porcentagem = (compras3000 / total_compras) * 100

print(f"Quantidade de compras acima de R$ 3000: {compras3000}")
print(f"Porcentagem quanto ao total: {porcentagem:.2f}%")