## o objetivo desta versão é limpar redundâncias

import time

def minuto_ou_hora():
    try:
        tipo_tempo = int(input("Escolha: 1- Segundos. 2- Minutos: "))
        if tipo_tempo == 1:
            return 1
        if tipo_tempo == 2:
            return 2
        else:
            print("Opção inválida.")
            quit()
    except:
        print("digito inválido.")
        quit()

def tempo_passado(a):
    if a == 1:
        segundos = int(input("Quantos segundos? "))
        b = segundos
        while b > 0:
            print(b)
            time.sleep(1)
            b -= 1
        print(f"tempo acabou. passaram-se f{segundos} segundos.")
    
    elif a == 2:
        minutos = float(input("Quantos minutos? "))
        b = minutos * 60
        while b > 0:
            print(b)
            time.sleep(1)
            b -= 1
        print(f"tempo acabou. Passaram-se {minutos} minutos.")
    else:
        print("Opção inválida.")

abacaxi = minuto_ou_hora()
tempo_passado(abacaxi)


