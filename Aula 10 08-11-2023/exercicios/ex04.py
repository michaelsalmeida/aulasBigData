import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

caminho = './Aula 10 08-11-2023/arquivos/company_sales_data.csv'

df = pd.read_csv(caminho)

listaMeses = df['month_number'].to_list()
vendasCremeDental = df['toothpaste'].to_list()

plt.xlabel('Meses')
plt.ylabel('Número de vendas')

plt.title('Vendas de creme dental')

plt.grid(True, linewidth = 1, linestyle = '--')



sns.scatterplot(x = listaMeses, y = vendasCremeDental)

plt.savefig('./Aula 10 08-11-2023/graficos-criados/ex04.png')
