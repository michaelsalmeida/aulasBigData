import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from funcoes import apagarArquivo

pasta = './Aula 09 06-11-2023/graficos-criados/'
df = pd.read_csv('./Aula 09 06-11-2023/arquivos/company_sales_data.csv')

df_meses = df['month_number'].to_list()
df_totalLucro = df['total_profit'].to_list()


plt.plot(df_meses, df_totalLucro, marker = '*', c = 'blue', mec = 'red')

plt.xlabel('Meses', fontsize = 16)
plt.ylabel('Lucro', fontsize = 16)

plt.title('Relatório lucro por mês', fontsize = 20)

apagarArquivo(pasta, 'ex01.png')

plt.savefig('./Aula 09 06-11-2023/graficos-criados/ex01.png')
