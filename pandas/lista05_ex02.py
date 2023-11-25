import pandas as pd
import os


#Crie um programa em pandas para ler o arquivo em Excel imobiliária.xlsx e coloque em um dataframe.

df = pd.read_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\arquivos\\imobiliária.xlsx')


# c) Visualize o cabeçalho dos dados;

# print(df.head())


# d) Visualize as últimas linhas;

# print(df.tail())

# e) Escreva um programa para renomear o cabeçalho da tabela com os seguintes nomes:

df.columns = [
    'Filial',
    'Vendedor',
    'Data',
    'Tipo',
    'Área (m²)',
    'Dorms.',
    'Garag.',
    'Piscina',
    'Preço',
    'Comissão'
]

# print(df.head())


# g) 5. Quais são os tipos de dados que temos no dataframe?

# print(df.info())


# h) 6. Há valores faltantes ou nulos?

# print(df.isnull())

# i) 7. Calcule a soma, média, máximo, mínimo e contagem da coluna Preço.

# soma = df['Preço'].sum()
# media = df['Preço'].mean()
# maximo = df['Preço'].max()
# minimo = df['Preço'].min()
# contagem = df['Preço'].count()

# print(f'A soma dos Preços é igual a R${soma:.2f}')
# print(f'A média dos preços é igual a R${media:.2f}')
# print(f'O valor máximo registrado é igual a R${maximo:.2f} e o valor mínimo foi o R${minimo}')
# print(f'Foram analizados {contagem} campos preenchidos')


# df_centro = df[df['Filial'] == 'Centro']
# print(df[df['Filial'] == 'Centro'])


# df_centro.to_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\relatorios-filiais\\Centro.xlsx')


# df_noroeste = df[df['Filial'] == 'Noroeste']

# print(df_noroeste)

# df_noroeste.to_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\relatorios-filiais\\Noroeste.xlsx')


# df_norte = df[df['Filial'] == 'Norte']

# print(df_norte)

# df_norte.to_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\relatorios-filiais\\Norte.xlsx')

# df_Sudeste = df[df['Filial'] == 'Sudeste']

# print(df_Sudeste)

# df_Sudeste.to_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\relatorios-filiais\\Sudeste.xlsx')

# df_Oeste = df[df['Filial'] == 'Oeste']

# print(df_Oeste)

# df_Oeste.to_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\relatorios-filiais\\Oeste.xlsx')

# df_Leste = df[df['Filial'] == 'Leste']

# print(df_Leste)

# df_Leste.to_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\relatorios-filiais\\Leste.xlsx')

# df_Sudoeste = df[df['Filial'] == 'Sudoeste']

# print(df_Sudoeste)

# df_Sudoeste.to_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\relatorios-filiais\\Sudoeste.xlsx')

# df_Sul = df[df['Filial'] == 'Sul']

# print(df_Sul)

# df_Sul.to_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\relatorios-filiais\\Sul.xlsx')

# df_Nordeste = df[df['Filial'] == 'Nordeste']

# print(df_Nordeste)

# df_Nordeste.to_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\relatorios-filiais\\Nordeste.xlsx')

'''
l) Gere um arquivo em Excel para representar as vendas efetuadas pela filial norte
em 2010.

'''

# df_filial = df[(df['Filial'] == 'Norte')&(df['Data'] >= '2010-01-01')&(df['Data'] <= '2010-12-31')]


# caminho = './relatorios-filiais/filial-datas'

# if (not os.path.exists(caminho)):
#     os.mkdir('./relatorios-filiais/filial-datas')
   
    
# df_filial.to_excel('./relatorios-filiais/filial-datas/Norte_2010.xlsx')


'''
m) Gere um arquivo em Excel para representar as vendas efetuadas pela filial
Sudeste em 2010. Sendo que no relatório deve conter apenas vendas de casas
sem garagem.

'''

# df[df['Filial'] == 'Sudeste'].info()

# df_filial = df[(df['Filial'] == 'Sudeste') & (df['Data'] >= '2010-01-01') & (df['Data'] <= '2010-12-31') & (df['Tipo'] == 'Casa') & (df['Garag.'] == 0)]

# df_filial.to_excel('./relatorios-filiais/filial-datas/Sudeste_2010_casa_semGaragem.xlsx')


'''
n) Qual o valor máximo de comissão que a imobiliária numa venda?
'''

print(df[df['Comissão']==df['Comissão'].max()])

# print(f'Valor máximo de comissão foi de R${maiorComissao}')


'''
o) Quantas casas de 2 ou 3 dormitórios foram vendidas pelo Ricardo antes de 2011.
'''

# df_ricardo = df[(df['Vendedor'] == 'Ricardo') & (df['Tipo'] == 'Casa') & (df['Dorms.'] >= 2) & (df['Dorms.'] <= 3) & (df['Data'] < '2011-01-01')]

# df_ricardo.to_excel('./relatorios-filiais/filial-datas/Ricardo.xlsx')

