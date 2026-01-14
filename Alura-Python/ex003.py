"""
Faça como eu fiz: saudação personalizada
 Próxima Atividade

Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

Se for antes das 12h, exibir "Bom dia";

Entre 12h e 18h, exibir "Boa tarde";

Após 18h, exibir "Boa noite"."""


def horario_de_atendimento(nome, horario):
    if horario <= 12:
      print(f'Bom dia! {nome}')
    elif horario <= 17:
      print(f'Boa tarde! {nome}')
    elif horario >= 18:
      print(f'Boa noite! {nome}')

nome = str(input('Digite o seu nome: '))
horario = int(input('Digite a hora atual (0-23):\n'))
horario_de_atendimento(nome, horario)