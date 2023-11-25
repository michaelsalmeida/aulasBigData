'''
Crie uma variável chamada "peso" e atribua um valor numérico a ela.
Verifique se o peso está dentro do intervalo de 50 a 100 (inclusive) e imprima a
mensagem "Peso válido" ou "Peso inválido" de acordo com a condição.
'''


from funcoes import *


peso = coringa('Digite seu peso: ', float)

if 50 <= peso <= 100:
    print('Peso válido')

else:
    print('Peso inválido')