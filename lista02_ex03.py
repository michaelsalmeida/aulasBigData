'''
Crie duas variáveis, "nota1" e "nota2", e atribua valores numéricos a elas.
Verifique se a média das notas é maior ou igual a 7 e imprima "Aprovado" ou
"Reprovado" de acordo com a condição.

'''

from funcoes import *

n1 = coringa('Digite a primeira nota: ', float)
n2 = coringa('Digite a segunda nota: ', float)

media = (n1 + n2) / 2

print(f'Média desse aluno foi {media:.1f}')

if media >= 7:
    print(f'Aprovado')

else:
    print(f'Reprovado')