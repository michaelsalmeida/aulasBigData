from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

diabete = load_diabetes(return_X_y = True)

x, y = diabete

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.65, random_state = 42)


print(f'Dados de X para treinamento: {len(x_train)}')
print(f'Dados de Y para treinamento: {len(y_train)}')

print(f'Dados dr X para teste: {len(x_test)}')
print(f'Dados dr Y para teste: {len(y_test)}')
