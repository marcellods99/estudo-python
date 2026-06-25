#2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

empresa = [2172.54 , 3701.35 , 3518.08 , 3426.61 , 3249.38 , 2840.82 , 2840.82 , 3891.45 , 3075.26 , 2317.64 , 3219.08]

compras3000 = 0

for gasto in empresa:
    if gasto > 3000:
        compras3000 = compras3000 + 1   #se empresa tiver um número maior q 3000 mil, colocar na lista.

total_compras = len(empresa)
porcentagem = (compras3000 / total_compras) * 100

print(f'{compras3000}')
print(f'{porcentagem:.2f}')