import pandas as pd
import os


'''
b) Declare uma variável chamada dir_path para armazenar o caminho
dodiretório que contém os arquivos a serem combinados;
c) Crie uma lista vazia chamada res (repositório) para salvar a string do
caminho
+ nome dos arquivos salvas na pasta filais;
'''
diretorioArquivos = './relatorios-filiais/'

caminhoArquivos = []

arquivosDentroDaPasta = os.listdir(diretorioArquivos)


'''
d) Crie uma estrutura de repetição, utilizando FOR, para capturar o nome
dos arquivos que estão no repositório indicado na variável dir_path.
Nesta estrutura você deve utilizar o comando os.listdir, este comando
lista todos osarquivos que estão dentro de um determinado diretório.

Após listar estes arquivos, estes dados devem ser inseridos na variável
path e em seguida umaestrutura de decisão deve verificar se o que está
salvo neste diretório realmenteé um arquivo, para isto, utilize a estrutura
de decisão if com o comando os.path.isfile(diretório + nome do arquivo),
este comando verifica se o caminhoinformado realmente é um arquivo,
caso seja ele responde verdadeiro, caso contrário, responderá false.
Caso seja um arquivo, o caminho completo do arquivo deve ser inserido
à lista
res.
'''

for arquivo in arquivosDentroDaPasta:
    caminhoTotal = diretorioArquivos + arquivo

    if os.path.isfile(caminhoTotal):
        caminhoArquivos.append(caminhoTotal)


'''
e) Crie um dataframe vazio, e nomeie ele como files_combined.
files_combined = [ ]

Crie uma estrutura de repetição, utilizando o comando for. Nesta estrutura a
variável file deve capturar todos os caminhos dos arquivos que estão na lista res.
f) Dentro da estrutura de decisão crie um dataframe e nomeie o mesmo
como df1. Este data frame deve receber os arquivos listados na pasta,

para isto utilizeo comando pd.read_excel para ler os arquivos e atribuí-
los ao data frame. Após ler o arquivo, você deve concatenar o dataframe

files_combined com odf1.

g) Após agrupar os arquivos, converta o dataframe em Excel e salve o
mesmo com o seguinte nome: arquivosCombinados.xlsx.
for file in res:
df1 = pd.read_excel(variável com o caminho completo dos arquivos)
files_combined = pd.concat([dataframe 1 ,dataframe 2])


h) Faça o mesmo processo com os arquivos que estão na pasta vendas.
Reescreva o código com o objetivo de fixar a sequência lógica e sintaxe
dos comandos.
'''

#relarorio filiais
# files_combined = pd.DataFrame()

# for caminho in caminhoArquivos:
#     df1 = pd.read_excel(caminho)

#     files_combined = pd.concat([files_combined, df1])

# files_combined.to_excel(diretorioArquivos + 'arquivosCombinados.xlsx')

diretorioArquivosVendas = './lista05_ex04_arquivos/'

arquivosNaPasta = os.listdir(diretorioArquivosVendas)

caminhoArquivosVendas = []

for arc in arquivosNaPasta:
    if os.path.isfile(diretorioArquivosVendas + arc):
        caminhoArquivosVendas.append(diretorioArquivosVendas + arc)


files_combined2 = pd.DataFrame()

for cam in caminhoArquivosVendas:
    df2 = pd.read_excel(cam)

    files_combined2 = pd.concat([files_combined2, df2])


files_combined2.to_excel(diretorioArquivosVendas + 'arquivosCombinadosVendas.xlsx')
