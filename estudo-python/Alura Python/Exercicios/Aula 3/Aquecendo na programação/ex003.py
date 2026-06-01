"""
Questão 3
Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
"""

palavra = str(input('Digite uma letra: ')).lower()
vogal = 'aeiou'
cons = 'bcdfghjklmnpqrstvwxyz'
if palavra == vogal:
  print(f'{palavra} = a uma vogal.')
elif palavra == cons:
  print(f'{palavra} = a uma consoante')
else:
  print(f'Erro: Digite uma vogal ou uma consoante.')