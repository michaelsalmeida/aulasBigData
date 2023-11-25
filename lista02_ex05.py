'''
Crie uma variável chamada "numero" e atribua um valor inteiro a ela.
Verifique se o número é par ou ímpar e imprima a mensagem correspondente.
'''

from funcoes import *

numero = coringa('Digite um número qualquer: ', float)

if numero % 2 == 0:
    print(f'O número digitado é par')

else:
    print(f'O número digitado é ímpar')