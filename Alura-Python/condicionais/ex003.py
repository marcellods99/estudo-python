#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario = str(input('Nome do usuário: '))
senha = input('Senha do usuário: ')

nome_usuario = "noitepraia"
senha_usuario = "praiabonita"

if usuario == nome_usuario and senha == senha_usuario:
    print('Usuário correto')
else:
    print("Dados incorretos")