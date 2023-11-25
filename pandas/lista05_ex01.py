import pandas as pd

#a) Abra o arquivo world_happiness_report_2015.csv e o aloque em um dataframe.
df = pd.read_csv('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\arquivos\\world_happiness_report_2015.csv')


# ------------------------ b) Verifique o cabeçalho e o final do dataframe. ------------------------


# print(df.head())


# ------------------------ c) Quais as colunas desse dataframe? ------------------------


# print(df.head(0))


# ------------------------ d) Quais os tipos de dados temos no dataframe? ------------------------


# print(df.info())

# ------------------------ e) Há valores faltantes ou nulos? Em quais colunas? ------------------------

print(df[df.isnull()==True])


# ------------------------ f) Renomeie as variáveis como segue: ------------------------

# df = df.rename(columns={
#     'happiness rank' : 'rank_felicidade',
#     'happiness score' : 'score_felicidade',
#     'standard error' : 'stand_error',
#     'economy (GDP per Capita)' : 'PIB',
#     'health (Life Expectancy)' : 'expect_vida',
#     'trust (Government Corruption)' : 'corrupcao'
#     })

# print(df.head(0))


# ------------------------ g) Quais os valores médios de expect_vida? E o valor mediano? E o máximo da variável PIB? -----------------

# print(df.describe())