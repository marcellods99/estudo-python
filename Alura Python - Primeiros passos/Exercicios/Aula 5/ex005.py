#5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.


limite = int(input('Digite um número limite: '))
lista_primos = []

# 1. Passa por todos os números do caminho (ex: de 2 até 10)
for numero in range(2, limite + 1):
    
    # O nosso "interruptor": começamos acreditando que o número É primo
    e_primo = True 
    
    # 2. Testamos se o 'numero' divide por alguém menor que ele
    for divisor in range(2, numero):
        if numero % divisor == 0:
            e_primo = False # Opa! Dividiu por alguém, então NÃO é primo (desliga a luz)
            
    # 3. Se depois de todos os testes a luz continuou LIGADA, ele vai pra lista!
    if e_primo == True:
        lista_primos.append(numero)

print(lista_primos)