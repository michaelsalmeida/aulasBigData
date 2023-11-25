'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

from funcoes import *

x()

sexo = coringa('Digite seu sexo [M - Masculino / F - Feminino]', str).lower()

if sexo[0] == 'm':
    print('Sexo masculino digitado')

elif sexo[0] == 'f':
    print('Sexo feminino digitado')

else:
    print('Sexo inválido')