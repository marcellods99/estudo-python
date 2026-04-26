#3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

letra = str(input('Digite uma letra: ')).lower()

vogal = 'aeiou'
cons = 'bcdfghjklmnpqrstvwxyz'

if letra == vogal:
    print(f'{letra} É uma vogal!')
    if letra == cons:
        print(f'{letra} é uma consoante!')