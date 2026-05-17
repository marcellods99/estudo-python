##8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

faixa1 = [0] # 0-25
faixa2 = [0] # 26-50
faixa3 = [0] # 51-75
faixa4 = [0] # 76-100

print('Digite a idade dos pensionistas, se digitar número negativo encerra: ')

while True:
  try:
    idade = int(input("Idade: "))
    if idade < 0:
    # Condição de parada
      break
    if 0 <= idade <= 25:
            faixa1 += 1
    elif 26 <= idade <= 50:
            faixa2 += 1
    elif 51 <= idade <= 75:
            faixa3 += 1
    elif 76 <= idade <= 100:
            faixa4 += 1
    else:
      print('Idade fora do intervalo esperado (0-100). Ignorada.')
  except ValueError:
    print("Por favor, digite um número inteiro válido.")