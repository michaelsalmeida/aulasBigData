import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

caminho = './Aula 10 08-11-2023/arquivos/company_sales_data.csv'

df = pd.read_csv(caminho)

listaMeses = df['month_number'].to_list()
listaCremeFacial = df['facecream'].to_list()
listaLimpadorFacial = df['facewash'].to_list()

# sns.barplot(x = listaMeses, y = listaCremeFacial)
# sns.barplot(x = listaMeses, y = listaLimpadorFacial)

'''

Primeiro argumento : posicao da barra no eixo x
Segundo argumento : eixo y em si 
Terceiro argumento : largura da barra

'''

plt.bar([pos - 0.25 for pos in listaMeses], listaCremeFacial, width = 0.25)

plt.bar([pos + 0.25 for pos in listaMeses], listaLimpadorFacial, width = 0.25)

plt.savefig('./Aula 10 08-11-2023/graficos-criados/ex05.png')