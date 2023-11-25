import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


caminho = './arquivos/horasDeEstudo.csv'

df = pd.read_csv(caminho)

# print(df.head())

# print(df.tail())


# print(df.info())

# print(df.isnull().sum())

# print(df.describe())


'''
Correlação entre variáveis
'''
# print(df.corr())


'''
Criando gráfico de dispersão
'''

# plt.scatter(
#     data = df, # Data frame com os dados
#     x = 'horas_estudo_mes', # Coluna que será a preditora ( independente )
#     y = 'salario', # Variável resposta (a que será gerad de acordo com a coluna preditora )
#     label = 'Dados Reais Históricos', # Rótulo
#     color = 'gray' # Cor
# )

# plt.xlabel('Horas de estudo')
# plt.ylabel('Salário')

# plt.legend()

'''
Histograma para analizar o comportamento da variável ( x )
'''


# sns.histplot(
#     data = df,
#     x = 'horas_estudo_mes',
#     kde = True
# )

# plt.savefig('./graficos-gerados/explicacoes01.png')



x = df['horas_estudo_mes']
y = df['salario']

x = np.array(x)

x = x.reshape(-1, 1)



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# print(f'Quantidade de elementos para treino { len(x_train) }')
# print(f'Quantidade de elementos para teste { len(x_test) }')
# print(f'Quantidade de elementos totais { len(x) } ')

modelo = LinearRegression()

# Treinar modelo

modelo.fit(x_train, y_train)


# Exibir os coeficientes

# coeficiente angular ( o A da fórmula )
# print(modelo.coef)

# coeficiente linear ( o B da fórmula )

# print(modelo.intercept_)


# inserir os valores para a previsão


horasEstudo = np.array([[50], [48], [65], [73]])

# Realizar a previsão

salario = modelo.predict(horasEstudo)

print(salario[3])

# for n in range (0, 5):

#     print(f'Para { horasEstudo[n][0] } horas aplicadas ao estudo, tem uma probabilidade de você ter um salário de aproximadamente de R${ salario[n] }')