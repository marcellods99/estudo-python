#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
media = (primeira_nota + segunda_nota) / 2 #Calculo da média
print(f'Sua primeira nota foi: {primeira_nota}\nSua segunda nota foi: {segunda_nota}\nA média das duas foi: {media}')