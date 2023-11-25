import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from funcoes import apagarArquivo

pasta = './Aula 09 06-11-2023/graficos-criados/'

df = pd.read_csv('./Aula 09 06-11-2023/arquivos/company_sales_data.csv')

# Criando listas com base nas colunas do DataFrame

meses = df['month_number'].to_list()
faceCreamSalesData = df['facecream'].to_list()
faceWashSalesData = df['facewash'].to_list()
toothPasteSalesData = df['toothpaste'].to_list()
bathingSoapSalesData = df['bathingsoap'].to_list()
shampooSalesData = df['shampoo'].to_list()
moisturizerSalesData = df['moisturizer'].to_list()

# gerar um gráfico de linhas para plotar cada variável descrita acima
# Tipo de marcador = o | linewidth = 3

plt.plot(meses, faceCreamSalesData, label = 'Face Cream', marker = 'o', linewidth = 3)
plt.plot(meses, faceWashSalesData, label = 'Face Wash', marker = 'o', linewidth = 3)
plt.plot(meses, toothPasteSalesData, label = 'Tooth paste', marker = 'o', linewidth = 3)
plt.plot(meses, bathingSoapSalesData, label = 'Bathing soap', marker = 'o', linewidth = 3)
plt.plot(meses, shampooSalesData, label = 'Shampoo', marker = 'o', linewidth = 3)
plt.plot(meses, moisturizerSalesData, label = 'Moisturizer', marker = 'o', linewidth = 3)

plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000])

plt.legend(loc = 'upper left')

plt.xlabel('Meses')
plt.ylabel('Valor')

plt.savefig('./Aula 09 06-11-2023/graficos-criados/ex03.png')