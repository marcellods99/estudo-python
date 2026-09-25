#Peça um número ao usuário e mostre a tabuada dele de 1 até 10.

tabuada = int(input('Digite a tabuada: '))

for c in range(1,11):
    print(f'{tabuada} x {c} = {tabuada * c}')