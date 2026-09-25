"""
Questão 2
Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
"""

nome = 'Marcello Dias'
digite = str(input('Digite o nome \'Marcello Dias\': ')).title()
if digite == nome:
  print('Nome correto.')
else:
  print('Nome incorreto.')