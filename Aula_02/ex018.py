'''
Exercício 18 - Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$10'
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

'''

from funcoes import *

x()

valorPorHora = coringa('Quanto voce recebe por hora: ', int)
qtdHoraTrabalhada = coringa('Quantas horas trabalhadas: ', int)

salarioBruto = valorPorHora * qtdHoraTrabalhada

impostoDeRenda = (salarioBruto * 11) / 100

inss = (salarioBruto * 8) / 100

sindicato = (salarioBruto * 5) / 100

salarioliquido = salarioBruto - impostoDeRenda - inss - sindicato

print(f'Salario bruto -> R${salarioBruto:.2f}')
print(f'Desconto imposto de renda -> R${impostoDeRenda:.2f}')
print(f'Desconto INSS -> R${inss:.2f}')
print(f'Desconto Sindicato -> R${sindicato:.2f}')
print(f'\nSalário líquido -> R${salarioliquido:.2f}')
