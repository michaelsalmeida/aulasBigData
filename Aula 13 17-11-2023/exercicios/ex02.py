import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


caminho = './arquivos/advertising.csv'

dados = pd.read_csv(caminho)

# print(dados.info())

# print(dados.isnull().sum())

# print(dados.describe())

# fig, axs = plt.subplots(3, figsize = (5, 5))

# plt1 = sns.boxplot(dados['TV'], ax = axs[0], orient = 'h')
# plt2 = sns.boxplot(dados['Newspaper'], ax = axs[1], orient = 'h')
# plt3 = sns.boxplot(dados['Radio'], ax = axs[2], orient = 'h')
# plt.tight_layout()

# plt.scatter(
#     data = dados,
#     x = 'TV',
#     y = 'Sales',
#     label = 'Vendas relacionando TV',
#     color = 'red'
# )

# plt.xlabel('Televisão')
# plt.ylabel('Vendas')

# plt.legend()

# plt.savefig('./graficos-gerados/TV-Vendas.png')

# plt.scatter(
#     data = dados,
#     x = 'Newspaper',
#     y = 'Sales',
#     label = 'Vendas relacionando Newspaper',
#     color = 'red'
# )

# plt.xlabel('Newspaper')
# plt.ylabel('Vendas')

# plt.legend()

# plt.savefig('./graficos-gerados/Newspaper-Vendas.png')

# plt.scatter(
#     data = dados,
#     x = 'Radio',
#     y = 'Sales',
#     label = 'Vendas relacionando Radio',
#     color = 'red'
# )

# plt.xlabel('Radio')
# plt.ylabel('Vendas')

# plt.legend()

# plt.savefig('./graficos-gerados/Radio-Vendas.png')


# sns.heatmap(dados.corr(), cmap = 'YlGnBu', annot = True)

# plt.savefig('./graficos-gerados/grafico-calor-correlacao-vendas.png')

tv = np.array(dados['TV'])

sales = dados['Sales']

tv = tv.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(tv, sales, test_size = 0.3, random_state = 0)

modelo = LinearRegression()

modelo.fit(x_train, y_train)

valorTv = np.array([[200]])

correlacao = modelo.predict(valorTv)

print(correlacao)
