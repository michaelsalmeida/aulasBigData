def x ():
    from os import system
    from platform import platform

    if platform == "linux":
        system('clear')
    
    else:
        system('cls')

def z (time: int):
    from time import sleep

    sleep(time)


def coringa (txt = '', tipo = ''):
    while True:
        
        try:
            if tipo == '':
                a = input(txt)
            else:
                a = tipo(input(txt))
            
        except:
            x()
            print('Digite um valor válido')
            
        else:
            return a


def ptimer (txt, timer = 1):
    print(txt)
    z(timer)