import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from funcoes import apagarArquivo

arquivo = './Aula 09 06-11-2023/arquivos/DadosVendaCarros.xlsx'

df = pd.read_excel(arquivo)


df.columns = [
    'DataNotaFiscal',
    'Fabricante',
    'Estado',
    'ValorVenda',
    'ValorCusto',
    'TotalDesconto',
    'CustoEntrega',
    'CustoMaoDeObra',
    'NomeCliente',
    'Modelo',
    'Cor', 
    'Ano',
    'Mês'
]

'''
    DataNotaFiscal    Fabricante          Estado  ValorVenda  ValorCusto  TotalDesconto  CustoEntrega  CustoMaoDeObra                     NomeCliente       Modelo       Cor     Ano        Mês
0       04-10-2016   Rolls Royce       São Paulo     95000.0     50000.0          500.0         750.0           750.0                     Aldo Motors     Camargue  Vermelho  2016.0    Outubro
1       01-01-2016  Aston Martin       São Paulo    120000.0     75000.0            0.0        1500.0           550.0                     Honest John          DBS      Azul  2016.0    Janeiro
2       02-02-2016   Rolls Royce       São Paulo     88000.0     75000.0          750.0        1000.0           550.0                   Bright Orange  Prata Ghost     Verde  2016.0  Fevereiro
3       03-03-2016   Rolls Royce       São Paulo     89000.0     88000.0            0.0        1000.0           550.0                     Honest John  Prata Ghost      Azul  2016.0      Março
4       04-04-2016   Rolls Royce       São Paulo     92000.0     62000.0            0.0        1500.0           550.0                     Wheels'R'Us     Camargue     Prata  2016.0      Abril
..             ...           ...             ...         ...         ...            ...           ...             ...                             ...          ...       ...     ...        ...
490     23-09-2019  Aston Martin  Rio de Janeiro     39750.0     27500.0         1300.0         -75.0          1250.0  Buckingham Palace Car Services          DB9     Preto  2019.0   Setembro
491     24-10-2019  Aston Martin  Rio de Janeiro     40440.0     22500.0          550.0         175.0          1250.0  British Luxury Automobile Corp          DB9  Vermelho  2019.0    Outubro
492     25-11-2019   Rolls Royce  Rio de Janeiro     72000.0     22500.0         1050.0         -75.0           950.0                Classy Car Sales     Camargue      Azul  2019.0   Novembro
493     26-11-2019  Aston Martin  Rio de Janeiro     40440.0     36125.0          800.0         875.0          1250.0                 Ambassador Cars          DB9     Verde  2019.0   Novembro
494     27-11-2019  Aston Martin  Rio de Janeiro     77250.0     22500.0          550.0         875.0          1250.0                  Embassy Motors          DB9     Prata  2019.0   Novembro

[457 rows x 13 columns]
'''
df = df.dropna()

anos = df['Ano'].drop_duplicates().to_list()

vendas = {}

for ano in anos:
    df_ano = df[df['Ano'] == ano]

    valor = df_ano['ValorVenda'].sum()

    vendas[ano] = valor

plt.bar(vendas.keys(), vendas.values())
plt.xticks(anos)
plt.xlabel('Anos')
plt.ylabel('Valor (em milhões)')

plt.title('Carros vendidos por ano')

plt.savefig('./Aula 09 06-11-2023/graficos-criados/ex10.png')
