import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100) # Gerar 100 números entre 0 e 2 * pi
y = np.sin(x)
z = np.cos(x)

# plt.plot(x, y, label = 'Função seno', color = '#853DF2')
# plt.plot(x, z, label = 'Função cosseno',color = '#65CADB')

# plt.legend()

# plt.title('Funções trigonométricas')

# plt.xlabel('Valores de X')
# plt.ylabel('Valores de Y')

plt.subplot(2, 1, 1)

plt.plot(x, y, label = 'Função seno', color = '#853DF2')

plt.subplot(2, 1, 2)

plt.plot(x, z, label = 'Função cosseno',color = '#65CADB')

plt.savefig('./Aula 10 08-11-2023/graficos-criados/teste1.png')
