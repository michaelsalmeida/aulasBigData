import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


caminho = './Aula 12 13-11-2023/arquivos/cars.csv'

df = pd.read_csv(caminho)

# Excluir a orimeira tabela do data frame

# urilizamos o comando df.drop >> axis = 1 ( coluna ) >> axis = 0 ( linha )
df = df.drop(['Unnamed: 0'], axis = 1)

x = df.loc[:, 'dist'].values
y = df.loc[:, 'speed'].values

correlacao = np.corrcoef(x, y)

x = x.reshape(-1, 1)

modelo = LinearRegression()
modelo.fit(x, y)

# equivale ao b da formula F(x) = ax + b
# print(modelo.intercept_)

# equivale ao a da formula F(x) = ax + b
# print(modelo.coef_)


# prever a velocidade para a distância de 22 metros

print(modelo.predict([[22]]))

plt.scatter(x, y)

plt.plot(x, modelo.predict(x), color = 'red')

plt.savefig('aaaaa.png')