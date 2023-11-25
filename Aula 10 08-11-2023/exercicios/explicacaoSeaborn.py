import seaborn as sns
import matplotlib.pyplot as plt
from pylab import randn
import pandas as pd

caminho =  './Aula 10 08-11-2023/arquivos/sea-level.csv'

dados = pd.read_csv(caminho)

dados = dados.loc[6:,:]

dados.columns = [
     'Year',
     'CSIRO - Adjusted sea level (inches)',
     'CSIRO - Lower error bound (inches)',
     'CSIRO - Upper error bound (inches)',
     'NOAA - Adjusted sea level (inches)'
]

dados['Year'] = dados['Year'].astype(int)
dados['CSIRO - Adjusted sea level (inches)'] = dados['CSIRO - Adjusted sea level (inches)'].astype(float)
dados['CSIRO - Lower error bound (inches)'] = dados['CSIRO - Lower error bound (inches)'].astype(float)
dados['CSIRO - Upper error bound (inches)'] = dados['CSIRO - Upper error bound (inches)'].astype(float)
dados['NOAA - Adjusted sea level (inches)'] = dados['NOAA - Adjusted sea level (inches)'].astype(float)

ano = dados['Year'].to_list()
nivelMar = dados['CSIRO - Adjusted sea level (inches)'].to_list()

sns.scatterplot(x = ano, y = nivelMar)


plt.savefig('./Aula 10 08-11-2023/graficos-criados/ROLA.png')