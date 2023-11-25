import pandas as pd
import os


'''
a) Crie um dataframe, utilizando o arquivo dados-vendas.xlsx. Crie data frames
para dividir a planilha vendas em 4 arquivos. São eles:
Tabela Fato
- ID-Produto;
- ID-Loja;
- ID-Vendedor;
- Data;
- ValorVenda.

Tabela Produtos
- ID-Produto;
- Produto;
- Categoria;
- Segmento;
- Fabricante;

Tabela Lojas
- ID-Loja;
- Cidade;
- Estado

Tabelas Vendedor
- ID-Vendedor;
- Vendedores;

Salve todos os arquivos em Excel.
'''

caminho = './arquivos/dados-vendas.xlsx'

df = pd.read_excel(caminho)

df = df.rename(columns={'Loja' : 'ID-Loja', 'Vendedor' : 'Vendedores', 'Data Venda' : 'Data'})

# df_fato = df[['ID-Produto', 'ID-Loja', 'ID-Vendedor', 'Data', 'ValorVenda']]

# df_produtos = df[['ID-Produto', 'Produto', 'Categoria', 'Segmento', 'Fabricante']]

# df_lojas = df[['ID-Loja', 'Cidade', 'Estado']]

# df_vendedor = df[['ID-Vendedor', 'Vendedores']]

# caminhoSalvarArquivos = './lista05_ex04_arquivos/'

# arquivos = [df_fato, df_produtos, df_lojas, df_vendedor]
# arquivosName = ['df_fato', 'df_produtos', 'df_lojas', 'df_vendedor']

# for arquivo in range(0, len(arquivosName)):

#     nomeArquivo = f'{arquivosName[arquivo]}.xlsx'

#     arquivos[arquivo].to_excel(caminhoSalvarArquivos + nomeArquivo, sheet_name=arquivosName[arquivo])


'''
b) Com base na coluna Vendedor, construa um código que permita remover as
duplicadas da coluna informada, e na sequência, filtre o dataframe e gere um
relatório individual para cada vendedor. Para fazer isso, siga os procedimentos
a seguir:

1. Crie uma pasta chamada relatórios-vendedores;
2. Importe a biblioteca Pandas;
3. Declare uma variável chamada path para armazenar o caminho da
pasta criada;
4. Declare uma variável com o nome file para armazenar o nome doarquivo
que será manipulado;
5. Crie um dataframe chamado dados e utilize o comando pd.read_excel
para acessar o arquivo.
6. Visualize o cabeçalho do dataframe;
7. Crie um dataframe chamado df_vendedores, para atribuir valores a ele
você deve selecionar apenas a coluna Vendedores e remover as
duplicadas do mesmo. Confirme se realmente o comando removeu as
duplicadas.
Após isso, crie uma lista com o seguinte nome listaVendedores, essa
lista deve receber os dados do dataframe df_vendedores. Para isso,
você deve converter o dataframe em lista, utilize o comando
dataframe.tolist().
8. Construa uma estrutura de repetição (FOR) para que a variável
vendedor receba os nomes que estão na lista listaVendedores e filtre
o dataframe dados, utilizando a coluna Vendedores para que gere um
novo dataframe (df_final) para cada vendedor. Ainda na estrutura de
repetição, você deve inserir uma linha de código para gerar um arquivo
em Excel para cada vendedor, utilize o comando dataframe.to_excel.
você deve converter o dataframe em lista, utilize o
comando
dataframe.tolist().
9. Construa uma estrutura de repetição (FOR) para que a variável
vendedor receba os nomes que estão na lista listaVendedores
e filtreo dataframe dados, utilizando a coluna Vendedores para
que gere um novo dataframe (df_final) para cada vendedor.
Ainda na estrutura de repetição, você deve inserir uma linha de
código para gerar um arquivoem Excel para cada vendedor,


c) Repita esse procedimento para os campos Categoria, Segmento,
Fabricante, Cidade e Estado. Reescreva todo o código para cada
caso, com o objetivode exercitar a sintaxe dos comandos.

'''

listaMaior = ['Vendedores', 'Categoria', 'Segmento', 'Fabricante', 'Cidade', 'Estado']

for coluna in listaMaior:

    caminho = f'./relatorios-vendedores/{coluna}/'

    if (not os.path.exists(caminho)):
        os.mkdir(caminho)

    listVendedor = df[coluna].drop_duplicates().to_list()

    for vendedor in listVendedor:
        df_final = df[df[coluna] == vendedor]

        nomeArquivo = f'{vendedor}.xlsx'

        df_final.to_excel(caminho + nomeArquivo)


