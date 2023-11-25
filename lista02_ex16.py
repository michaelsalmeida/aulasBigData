from funcoes import *

n = []

for num in range (0, 3):
    a = coringa(f'Digite o {num + 1} número: ', int)

    n.append(a)

maior = 0
menor = n[0]

for numero in range (0, len(n)):
    if n[numero] > maior:
        maior = n[numero]

    if n[numero] < menor:
        menor = n[numero]


print(f'O maior numero digitado foi o {maior} e o menor é o {menor}')