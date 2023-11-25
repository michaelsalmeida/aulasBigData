'''
Crie uma variável chamada "ano" e atribua um valor inteiro
representando um ano. Verifique se o ano é bissexto (divisível por 4, mas não por 100,
exceto se for divisível por 400) e imprima a mensagem correspondente.
'''

from funcoes import *


ano = coringa('Digite um ano para saber se ele é bissexto: ', int)

if ano % 4 == 0 or ano % 100 == 0 and ano % 400 == 0:
    print(f'{ano} é um ano bissexto')

else:
    print(f'{ano} não é um ano bissexto')
