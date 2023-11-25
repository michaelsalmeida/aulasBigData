import matplotlib.pyplot as plt


languages:str = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']

popularidades:str = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

explosao = [0.1, 0, 0, 0, 0, 0]

cores = ['#65CADB', '#657FDB', '#657FDB', '#65DBC6', '#4A39DB', '#6865DB']

plt.pie(popularidades, labels = languages, autopct='%1.1f%%', shadow= True, explode= explosao, colors= cores)


plt.savefig('./Aula 10 08-11-2023/graficos-criados/teste1.png')