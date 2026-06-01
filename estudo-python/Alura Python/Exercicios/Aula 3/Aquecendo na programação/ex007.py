#7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

print('\n[1] - Manhã\n[2] - Tarde\n[3] - Noturno')
ask = str(input('\nQual turno você trabalha?\n'))

if ask == '1':
  print('Bom dia!')
elif ask == '2':
  print('Boa Tarde!')
elif ask == '3':
  print('Boa noite!')
else:
  print('Valor Inválido!')