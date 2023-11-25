# ETL - extrair, transformar e carregar(load)

import pandas as pd

# idades = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])


# print(type(idades)) #<class 'pandas.core.series.Series'>

# print(idades) # abaixo o output desse comando
'''
0     10    
1     20    
2     30    
3     40    
4     50    
5     60    
6     70    
7     80    
8     90    
9    100    
dtype: int64
'''

df = pd.read_excel('C:\\Users\\CT Desenvolvimento\\Desktop\\aulasBigData\\arquivos\\bank-full.xlsx', sheet_name='Sheet 1 - bank-full')

df.columns = [
'idade', 'job', 'estado civil', 'educação', 'default', 'balance', 'housing',
'empréstimo', 'contato', 'dia', 'mês', 'duração', 'campanha', 'pdays', 'previous',
'poutcome'
]

df = df.rename(columns={'idade' : 'IDADE', 'job' : 'Profissão'})

# sheet_name = qual aba do excel você quer mexer

print(df.describe(include=['O']))

