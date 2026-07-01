import matplotlib.pyplot as plt

dias = [1, 2, 3, 4, 5]
exercicios_feitos = [2, 1, 0, 3, 2]

plt.plot(dias, exercicios_feitos, marker='o', color='purple', linestyle='--')

plt.title('Meu Progresso de Estudos - Alura')
plt.xlabel('Dias de Estudo')
plt.ylabel('Quantidade de Exercícios')
plt.grid(True)

plt.show()