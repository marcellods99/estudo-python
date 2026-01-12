def calcular_idade(ano_de_nascimento, ano_atual):
  return ano_atual - ano_de_nascimento   
  
ano_de_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade_atual = ano_atual - ano_de_nascimento
print(f'Você nasceu no ano {ano_de_nascimento} e o ano atual é {ano_atual}!!\nLogo você tem: {idade_atual} anos!')