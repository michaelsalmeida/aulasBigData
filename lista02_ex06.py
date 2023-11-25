'''
Crie uma variável chamada "horario" e atribua um valor inteiro
representando a hora do dia (em formato 24 horas). Verifique se o horário está dentro
do período da manhã (das 6h às 12h), da tarde (das 12h às 18h) ou da noite (das 18h
às 23h) e imprima a mensagem correspondente.
'''


from funcoes import *


horario = coringa('Digite as horas: ', float)

if 0 <= horario < 6:
    print('Madrugada')

elif 6 <= horario <= 12:
    print('Dia')

elif 13 <= horario <= 18:
    print('Tarde')

elif 19 <= horario <=23:
    print('Noite')

    