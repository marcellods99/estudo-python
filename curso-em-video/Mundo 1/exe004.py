#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

digite_algo = input('Digite qualquer coisa: ')
#Type para declarar o tipo primitivo
print('O tipo primitivo desse valor é ', type(digite_algo))
print('Só tem espaços? ', digite_algo.isspace())
print('É um número? ', digite_algo.isnumeric())
print('É alfabético? ', digite_algo.isalpha())
print('É alfanúmerico? ', digite_algo.isalnum())
print('Está em maiúsculas? ',digite_algo.isupper())
print('Está em minúsculas? ', digite_algo.islower())
print('Está com capslock? ', digite_algo.istitle())