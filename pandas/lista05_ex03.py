import pandas as pd
import os

'''
a) Crie um programa em pandas para ler o arquivo em Excel vendas.xlsx e
b) coloque em um dataframe.

'''
df = pd.read_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\arquivos\\Vendas.xlsx')

'''
c) Visualize o cabeçalho dos dados;
'''

# print(df.head())

'''
d) Visualize as últimas linhas;

'''

# print(df.tail())

'''
e) Escreva um programa para renomear o cabeçalho da tabela com os
f) seguintes nomes:

g) Quais são os tipos de dados que temos no dataframe?
h) Há valores faltantes ou nulos?

'''

df.columns = [
    'Data',
    'Vendedor',
    'Cargo',
    'Cliente',
    'UF',
    'Vendas'
]

# print(df.info())

'''
i) Calcule a soma, média, máximo, mínimo e contagem da coluna Vendas.
'''

# soma = df['Vendas'].sum()
# media = df['Vendas'].mean()
# maximo = df['Vendas'].max()
# minimo = df['Vendas'].min()
# contagem = df['Vendas'].count()

# print(f'Soma = R${soma:.2f}\nMedia = R${media:.2f}\nMáximo = R${maximo:.2f}\nMinimo = R${minimo:.2f}\nContagem = R${contagem:.2f}')


'''
j) Crie um programa para criar um dataframe para mostrar as vendas por cargo, e
salvar um arquivo em csv para com o nome de cada cargo:
▪ Supervisor de Vendas Pl
▪ Gerente Regional Jr.
▪ Supervisor de Vendas Sr
▪ Coordenador de Vendas Pl.
▪ Vendedor Jr.
▪ Vendedor Sr.
▪ Vendedor Pl.
▪ Gerente Regional Pl.
▪ Coordenador de Vendas Sr.
▪ Coordenador de Vendas Jr.
▪ Supervisor de Vendas Jr.

'''

# cargos = [
#     'Supervisor de Vendas Pl', 
#     'Gerente Regional Jr.', 
#     'Supervisor de Vendas Sr', 
#     'Coordenador de Vendas Pl.',
#     'Vendedor Jr.',
#     'Vendedor Sr.',
#     'Vendedor Pl.',
#     'Gerente Regional Pl.',
#     'Coordenador de Vendas Sr.',
#     'Coordenador de Vendas Jr.',
#     'Supervisor de Vendas Jr.'
#     ]

# for cargo in cargos:
#     df_cargo = df[df['Cargo'] == cargo]

#     caminho = './ex03_relatoriosCargo/'
#     nomeArquivo = f'{cargo}.csv'

#     df_cargo.to_csv(caminho + nomeArquivo)



'''
9. Crie um dataframe para cada coluna, contendo dados únicos.
'''


# df_data = df['Data'].drop_duplicates()
# df_vendedor = df['Vendedor'].drop_duplicates()
# df_cargo = df['Cargo'].drop_duplicates()
# df_cliente = df['Cliente'].drop_duplicates()
# df_uf = df['UF'].drop_duplicates()
# df_vendas = df['Vendas'].drop_duplicates()

# print(df_data, df_vendedor, df_cargo, df_cliente, df_uf, df_vendas)

