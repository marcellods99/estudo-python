#Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

def calcular_idade(ano_de_nascimento, ano_atual):
  return ano_atual - ano_de_nascimento   
  
ano_de_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade_atual = ano_atual - ano_de_nascimento
print(f'Você nasceu no ano {ano_de_nascimento} e o ano atual é {ano_atual}!!\nLogo você tem: {idade_atual} anos!')

#blablabla