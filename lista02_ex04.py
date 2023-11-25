'''
Crie uma variável chamada "idade" e atribua um valor inteiro a ela.
Verifique se a idade está dentro do intervalo de 18 a 30 (inclusive) e imprima a
mensagem "Idade válida" ou "Idade inválida" de acordo com a condição.

'''

from funcoes import *

idade = coringa('Digite sua idade: ', int)


if 18 <= idade <= 30:
    print(f'Idade válida')

else:
    print(f'Idade inválida')

    