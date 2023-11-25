import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import time


caminhoArquivo = './Aula 11 10-11-2023/arquivos/dados-satisfação.xlsx'

df = pd.read_excel(caminhoArquivo, sheet_name = 'treino')


df['Elogio a Instituição'] = df['Elogio a Instituição'].replace('SIM', 1)
df['Elogio a Instituição'] = df['Elogio a Instituição'].replace('NÃO', 0)




df['Elogio quanto ao app'] = df['Elogio quanto ao app'].replace('SIM', 1)
df['Elogio quanto ao app'] = df['Elogio quanto ao app'].replace('NÃO', 0)
df['Elogio quanto ao app'] = df['Elogio quanto ao app'].replace('NAO', 0)



df['Reclamação quanto ao app'] = df['Reclamação quanto ao app'].replace('SIM', 1)
df['Reclamação quanto ao app'] = df['Reclamação quanto ao app'].replace('NÃO', 0)

df['Reclamação a Instituição'] = df['Reclamação a Instituição'].replace('SIM', 1)
df['Reclamação a Instituição'] = df['Reclamação a Instituição'].replace('NÃO', 0)

df['Não Classificável'] = df['Não Classificável'].replace('SIM', 1)
df['Não Classificável'] = df['Não Classificável'].replace('NÃO', 0)



df['Elogio a Instituição'] = df['Elogio a Instituição'].astype(int)
df['Elogio quanto ao app'] = df['Elogio quanto ao app'].astype(int)

# match case = 1.0988423824310303
# if e elif = 1.169593334197998

# start_time = time.time()

# for valor in df['Classificação'].to_list():
#     match valor:
#         case 1:
#             actual = 1
#             resulado = -1

#         case 2:
#             actual = 2
#             resultado = -1

#         case 3:
#             actual = 3
#             resultado = 0

#         case 4:
#             actual = 4
#             resultado = 1
        
#         case 5:
#             actual = 5
#             resultado = 1

#     df['Classificação'] = df['Classificação'].replace(actual, resultado)
    
df['Classificação'] = df['Classificação'].replace(2, -1)
df['Classificação'] = df['Classificação'].replace(1, -1)
df['Classificação'] = df['Classificação'].replace(5, 1)
df['Classificação'] = df['Classificação'].replace(4, 1)
df['Classificação'] = df['Classificação'].replace(3,0)

# lista = df['Classificação'].drop_duplicates().to_list()
# print('AQUIIIII', lista)
# for valor in lista:

#     match valor:
#         case 1:
#             actual = 1
#             resulado = -1

#         case 2:
#             actual = 2
#             resultado = -1

#         case 3:
#             actual = 3
#             resultado = 0

#         case 4:
#             actual = 4
#             resultado = 1
        
#         case 5:
#             actual = 5

#             resultado = 1
#     df['Classificação'] = df['Classificação'].replace(valor, resultado)

    

# end_time = time.time()

# tempoExecucao = end_time - start_time

# print(f'Tempo de execução foi de {tempoExecucao}')

df_classificacao = df.groupby(['Instituição'])['Classificação'].agg('mean').reset_index()

df_classificacao['Classificação'] = df_classificacao['Classificação'] * 100

sns.barplot(x = df_classificacao['Instituição'], y = df_classificacao['Classificação'])

plt.savefig('./Aula 11 10-11-2023/arquivos/dados-satisfação.xlsx')