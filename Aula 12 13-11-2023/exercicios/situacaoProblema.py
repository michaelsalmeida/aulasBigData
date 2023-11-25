import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

caminho = './Aula 12 13-11-2023/arquivos/IceCreamData.csv'

dados = pd.read_csv(caminho)

# # cabeçalho

# print(dados.head())

# # ultima linhas

# print(dados.tail())

# # descrição

# print(dados.describe())

# # informação dos dados

# print(dados.info())


# Gerando visualizações gráficas 

# sns.jointplot(data = dados, x = 'Temperature', y = 'Revenue', color = 'gray')


# plt.savefig('./Aula 12 13-11-2023/graficos-criados/situacaoProblema.png')

# sns.pairplot(dados)

# plt.savefig('./Aula 12 13-11-2023/graficos-criados/situacaoProblema2.png')

# sns.lmplot(x = 'Temperature', y = 'Revenue', data = dados)

# plt.savefig('./Aula 12 13-11-2023/graficos-criados/situacaoProblema3.png')



'''
Criar e testar o modelo
'''

# Criação da vaariável deoendente (Y) > resposta
y = dados[['Revenue']]

# Criação da variável independente (X) > entrada
x = dados[['Temperature']]


'''
Separar dados teste e treino
'''

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)


modelo = LinearRegression()

modelo.fit(x_train, y_train)


print(f'Coeficiente linear (b): {modelo.intercept_}')
print(f'Coeficiente linear (b): {modelo.coef_}')


y_predict = modelo.predict(x_test)

print(y_predict)