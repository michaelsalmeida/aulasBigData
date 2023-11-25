'''
Faça um Programa que verifique se uma letra digitada é vogal ou
consoante.
'''

from funcoes import *

x()

vogais = 'aeiou'

letra = coringa('Digite uma letra: ', str).lower()

if letra == '':
    print(f'Campo vazio')

elif letra in vogais:
    print(f'Letra é vogal')

else:
    print(f'letra é consoante')