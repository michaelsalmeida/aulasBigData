'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

from funcoes import *

x()


n1 = coringa('Digite o primeiro número: ', float)
n2 = coringa('Digite o segundo número: ', float)

if n1 > n2:
    print(f'{n1} foi o maior número digitado')

else:
    print(f'{n2} foi o maior número digitado')