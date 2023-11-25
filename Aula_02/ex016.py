'''
Exercício 16 - Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:

a) o produto do dobro do primeiro com metade do segundo.
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.

'''
from funcoes.funcoes import *

x()


n1 = coringa('Digite o primeiro número (inteiro) : ', 'int')
n2 = coringa('Digite o segundo número (inteiro) : ', 'int')
n3 = coringa('Digite o terceiro número (real) : ', 'float')


a = (n1 * 2) * (n2 / 2)
b = (3 * n1) + n3
c = n3 ** 3


print(f'o produto do dobro do {n1} com metade do {n2} é igual a {a}')
print(f'a soma do triplo do {n1} com o {n3} é igual a {b}')
print(f'o {n3} elevado ao cubo é igual a {c}')