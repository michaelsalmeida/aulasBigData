import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from funcoes import apagarArquivo

pasta = './Aula 09 06-11-2023/graficos-criados/'

df = pd.read_csv('./Aula 09 06-11-2023/arquivos/company_sales_data.csv')

df_meses = df['month_number'].to_list()
df_lucros = df['total_profit'].to_list()

plt.plot(df_meses, df_lucros, c = 'red', ls = '--', mec = 'black', label = 'Total vendido por mês', marker = 'o', markerfacecolor = 'k', linewidth = 3)

plt.xlabel('Month Number', fontsize = 12)
plt.title('Company Sales data of last year')

plt.yticks([100000, 200000, 300000, 400000, 500000]) # Ajustando os intervalos do eixo Y
plt.xticks(df_meses) # Ajustando os intervalos do eixo X

plt.legend('aaaaaaa', loc = 'lower right')

apagarArquivo(pasta, 'ex02.png')

plt.savefig('./Aula 09 06-11-2023/graficos-criados/ex02.png')
