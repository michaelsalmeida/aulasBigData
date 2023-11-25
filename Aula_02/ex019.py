'''
Exercício 19 - Faça um programa para uma loja de tintas. O programa deverá pedir o
tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da
tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total.
'''

from funcoes import *

x()

largura = coringa('Digite a largura da parede: ', float)
altura = coringa('Digite a altura da parede: ', float)

area = largura * altura

litrosNecessarios = round(area / 3)

while True:
    if litrosNecessarios <= 18:
        latasDeTinta = 1

    else:
        latasDeTinta = round(litrosNecessarios / 18)

    break

valorPago = latasDeTinta * 80

ptimer(f'Sua parede possui {area}m².')

ptimer(f'Será necessário {litrosNecessarios}L de tinta para pintar sua parede\ne custará R${valorPago:.2f}.')