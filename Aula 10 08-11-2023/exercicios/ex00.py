import matplotlib.pyplot as plt

x = [-3, -2.5, -2, -1, 0, 1, 2, 2.5, 3]
y = [-27, -15.62, -8, -1, 0, 1, 8, 15.62, 27]

plt.plot(x, y, label = 'Função Cúbica', color = '#FF00FF')

plt.xlabel('Valor de X', fontsize = 15)
plt.ylabel('Valor de Y', fontsize = 15.5)

plt.legend(fontsize = 20)


plt.savefig('./Aula 10 08-11-2023/graficos-criados/ex00.png')