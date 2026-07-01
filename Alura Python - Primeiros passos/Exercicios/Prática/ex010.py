#1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().

empresa = [2172.54 , 3701.35 , 3518.08 , 3426.61 , 3249.38 , 2840.82 , 2840.82 , 3891.45 , 3075.26 , 2317.64 , 3219.08]

soma = sum(empresa)  #soma de todos os números da lista
tamanho = len(empresa)   # len diz a quantidade de itens que tem dentro da chave
media = soma / tamanho   # faz a média

print(f'A média de gastos é: {media:.2f}')