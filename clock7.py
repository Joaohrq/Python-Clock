## otimizando para garantir melhor uso para as funções.

import time

def minuto_ou_hora():
    try:
        tipo_tempo = int(input("Escolha: 1- Segundos. 2- Minutos: "))
        if tipo_tempo == 1:
            return 1
        elif tipo_tempo == 2:
            return 2
        else:
            print("Opção inválida.")
            quit()
    except ValueError:
        print("digito inválido. Escolha entre 1 e 2.")
        quit()

def tempo(a):
    if a == 1:
        try:
            segundos = int(input("Quantos segundos? "))
            if segundos <= 0:
                print("Digite números maiores que 0.")
                quit()
            return segundos
        except ValueError:
            print("Digite apenas números inteiros.")
            quit()
    elif a == 2:
        try:
            minutos = float(input("Quantos minutos? "))
            if minutos <= 0:
                print("Digite números maiores que 0.")
                quit()
            return minutos
        except ValueError:
            print("Digite apenas números.")
            quit()
    
    
def passar_tempo(a, b): ## a = tipo de tempo, b = quantidade de tempo
    if a == 1:
        if b == 1:
            while b > 0:
                print(b)
                time.sleep(1)
                b -= 1
            print("Tempo acabou. passou 1 segundo.")
        elif b > 1:
            c = b
            while c > 0:
                print(c)
                time.sleep(1)
                c -= 1
            print(f"Tempo acabou. Passaram-se {b} segundos.")
    
    elif a == 2:
        if b == 1:
            c = b * 60
            while c > 0:
                print(c)
                time.sleep(1)
                c -= 1
            print("Tempo acabou. passou 1 minuto.")
        elif b > 1:
            c = b * 60
            while c > 0:
                print(c)
                time.sleep(1)
                c -= 1
            print(f"Tempo acabou. Passaram-se {b} minutos.") 



abacaxi = minuto_ou_hora()
tmp = tempo(abacaxi)
passar_tempo(abacaxi, tmp)