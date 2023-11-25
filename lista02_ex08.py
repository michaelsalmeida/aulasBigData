'''

Crie uma variável chamada "numero" e atribua um valor inteiro a ela.
Verifique se o número é múltiplo de 3 e de 5 ao mesmo tempo e imprima a mensagem
correspondente.
'''

from funcoes import *


numero = coringa('Digite um número qualquer: ', int)

if numero % 3 == 0 and numero % 5 == 0:
    print(f'O {numero} múltiplo de 3 e 5 ao mesmo tempo')

else:
    print('Esse número não é multiplo de 3 e 5 ao mesmo tempo')