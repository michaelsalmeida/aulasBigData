import pandas as pd
import os
'''
         country                           region  happiness rank  happiness score  ...  freedom  trust (Government Corruption)  generosity  dystopia residual
0    Switzerland                   Western Europe               1            7.587  ...  0.66557                        0.41978     0.29678            2.51738
1        Iceland                   Western Europe               2            7.561  ...  0.62877                        0.14145     0.43630            2.70201
2        Denmark                   Western Europe               3            7.527  ...  0.64938                        0.48357     0.34139            2.49204
3         Norway                   Western Europe               4            7.522  ...  0.66973                        0.36503     0.34699            2.46531
4         Canada                    North America               5            7.427  ...  0.63297                        0.32957     0.45811            2.45176
..           ...                              ...             ...              ...  ...      ...                            ...         ...                ...
159       Rwanda               Sub-Saharan Africa             154            3.465  ...  0.59201                        0.55191     0.22628            0.67042
160        Benin               Sub-Saharan Africa             155            3.340  ...  0.48450                        0.08010     0.18260                NaN
161        Syria  Middle East and Northern Africa             156            3.006  ...  0.15684                        0.18906     0.47179            0.32858
162      Burundi               Sub-Saharan Africa             157            2.905  ...  0.11850                        0.10062     0.19727                NaN
163         Togo               Sub-Saharan Africa             158            2.839  ...  0.36453                        0.10731     0.16681                NaN

'''


'''
a) Abra o arquivo World Happiness.
'''
arquivoTrabalhado = './arquivos/world_happiness_report_2015.csv'

df = pd.read_csv(arquivoTrabalhado)

'''
b) Qual a média do score_felicidade?
'''

df = df.rename(columns={
    'happiness rank' : 'rank_felicidade',
    'happiness score' : 'score_felicidade',
    'standard error' : 'stand_error',
    'economy (GDP per Capita)' : 'PIB',
    'health (Life Expectancy)' : 'expect_vida',
    'trust (Government Corruption)' : 'corrupcao'
    })


# media = df['score_felicidade'].mean()

# print(f'A média de pontiação do score_felicidade é {media}')

'''
c) Qual a soma do PIB?
'''

# somaPib = df['PIB'].sum()

# print(f'A soma dos PIBs dessa basse de dados é igual a {somaPib}')

'''
d) Qual a soma do freedom e corrupção?
'''

# somaFreedom = df['freedom'].sum()
# somaCorrupcao = df['corrupcao'].sum()

# print(f'Soma corrupção = {somaCorrupcao}\nSoma Freedom = {somaFreedom}')


'''
e) Há dados duplicados? Quantos? Verifique quais são eles?
'''

# duplicados = df[df.duplicated(keep=False)]
# print(duplicados)

'''
f) Verifique a quantidade de dados faltantes.
'''

# df.info()

'''
g) Crie um dataframe onde os valores faltantes de score_felicidade sejam
substituídos por -9999.
'''

# df['score_felicidade'].fillna(-9999, inplace=True)

# df.info()


'''
h) Quantas e quais são as regiões existentes nos dados?
'''

# regioes = df['region'].drop_duplicates()

# quantidade = regioes.count()

# print(f'A base de dados possui {quantidade} regiões e são elas:')
# print(regioes)

'''
i) Verifique a frequência dos dados segundo suas regiões. Qual a região com maior
quantidade de dados? E a região com a menor quantidade?
'''
# regioes = df['region'].drop_duplicates()

# listaRegioes = regioes.to_list()

# maiorQuantidade = []
# menorQuantidade = []

# contador = 0

# for regiao in listaRegioes:
#     contagem = df[df['region'] == regiao].count().sum()

#     if contador == 0:
#         maiorQuantidade = [listaRegioes[contador], contagem]
#         menorQuantidade = [listaRegioes[contador], contagem]
#         contador += 1

#     elif contagem > maiorQuantidade[1]:
#         maiorQuantidade = [listaRegioes[contador], contagem]
#         contador += 1

#     elif contagem < menorQuantidade[1]:
#         menorQuantidade = [listaRegioes[contador], contagem]
#         contador += 1

# print(f'A região que possui a maior contagem de dados é a região {maiorQuantidade[0]} com {maiorQuantidade[1]} dados registrados')
# print(f'A região que possui a menor contagem de dados é a regiao {menorQuantidade[0]} com {menorQuantidade[1]} dados registrados')
