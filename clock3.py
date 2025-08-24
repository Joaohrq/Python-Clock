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
    except:
        print("digito inválido.")

def tempo_correr(a):
    if a == 1:
        segundos = int(input("Quantos segundos? "))
        return segundos
    if a == 2:
        minutos = int(input("Quantos minutos? "))
        return minutos

def segundos_passados(b):
    c = 0
    while c < b:
        print(c)
        time.sleep(1)
        c += 1
    if b > 1:
        print(f"Contagem acabou. Passaram-se {b} segundos.")
    elif b == 1:
        print("Contagem acabou, passou 1 segundo.")

def minutos_passados(d):
    f = d * 60
    e = 0
    while e < f:
        print(e)
        time.sleep(1)
        e += 1
    if d > 1:
        print(f"Contagem acabou. Passaram-se {d} minutos.")
    elif d == 1:
        print("Contagem acabou, passou 1 minuto.")


min_ou_hora = minuto_ou_hora()

if min_ou_hora == 1:
    tempo_a_correr = tempo_correr(min_ou_hora)
    segundos_passados(tempo_a_correr)

if min_ou_hora == 2:
    tempo_a_correr = tempo_correr(min_ou_hora)
    minutos_passados(tempo_a_correr)