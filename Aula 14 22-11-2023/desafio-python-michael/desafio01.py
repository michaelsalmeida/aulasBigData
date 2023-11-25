import pandas as pd                     # LER E MANIPULAR ARQUIVOS DISTINTOS
import os                               # GERENCIAR O SISTEMA OPERACIONAL
import matplotlib.pyplot as plt         # VISUALIZAR DADOS DE FORMA GRÁFICA
import seaborn as sns                   # VISUALIZAR DADOS DE FORMA GRÁFICA

######################## CARREGAR OS ARQUIVOS DE VENDAS ###############################


# PASTA QUE CONTÉM TODOS OS ARQUIVOS
# caminhoDaPasta = './arquivos/vendas/'

# ######## AGRUPAR TODOS OS DOCUMENTOS EM UM ÚNICO DATAFRAME ############

# diretorios = []         # Lista Vazia

# # LOCALIZAR OS ARQUIVOS E COMBINAR COM O CAMINHO DA PASTA
# for file in os.listdir(caminhoDaPasta):
#     fullPath = caminhoDaPasta + file
#     diretorios.append(fullPath)
    
# # CRIAR UM DATAFRAME VAZIO
# dfVendas = pd.DataFrame()

# # LOOP PARA ACESSAR OS DOCUMENTOS E COMBINÁ-LOS (+/- UNION DO SQL)

# for path in diretorios:
#     df = pd.read_excel(path)
#     dfVendas = pd.concat([dfVendas,df])
    
# # GERAR UM ARQUIVO CSV COM OS DADOS CONSOLIDADOS
# dfVendas.to_csv(caminhoDaPasta + 'arquivoCombinado.csv')



######################## CARREGAR OS DEMAIS DATAFRAMES ###################################
dfVendas = pd.read_csv('./arquivos/arquivoCombinado.csv')
dfMetas = pd.read_excel('./arquivos/base-meta-new.xlsx')
dfVendedores = pd.read_excel('./arquivos/Dimensões.xlsx',sheet_name='Vendedor')
dfProdutos = pd.read_excel('./arquivos/Dimensões.xlsx',sheet_name='Produto')
dfDatas = pd.read_excel('./arquivos/Dimensões.xlsx',sheet_name='Data')
dfGrupoProduto = pd.read_excel('./arquivos/Dimensões.xlsx',sheet_name='GrupoProduto')
dfClientes = pd.read_excel('./arquivos/Dimensões.xlsx',sheet_name='Cliente')

################# TRATAMENTO DO DATAFRAME METAS ############################

# FATIAMENTO DO DATAFRAME
dfMetas = dfMetas.iloc[3:,1:4]

# RENOMEAR COLUNAS
dfMetas.columns = ['cdVendedor','data','meta']

dfMetas

# MESCLANDO AS TABELAS VENDAS E DATAS COM PD.MERGE

df_result = pd.merge(
                dfVendas[['DataEmissao','QtdItens','ValorUnitario']],
                dfDatas[['Data','Ano']],
                left_on='DataEmissao',
                right_on='Data'
            )

# ADICIONAR A COLUNA SUBTOTAL AO DATAFRAME
df_result['subtotal'] = df_result['QtdItens'] * df_result['ValorUnitario']

# AGRUPAR OS DADOS POR ANO
df_result = df_result[['Ano','subtotal']].groupby('Ano').sum().reset_index()

# CRIAR O GRÁFICO
sns.barplot(
    data=df_result,
    x = 'Ano',
    y = 'subtotal')

plt.title('Vendas por ano')
plt.xlabel('Anos')
plt.ylabel('Vendas')

plt.savefig('./grafico01.png')