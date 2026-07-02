from random import choices as ch #AS altera o nome do import, deixando mais legível e menos poluído

estudantes_2 = ["João", "Maria", "José", "Ana"]
estudantes = ch(estudantes_2) #Usa biblioteca choices para sortear um nome

print(estudantes)