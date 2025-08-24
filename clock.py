import time


Tipo_tempo = int(input('Escolha: 1 - Segundos, 2- Minutos: '))

if Tipo_tempo == 1:
    segundos = int(input('quantos segundos?: '))
    a = 0
    while a < segundos:
       print(a)
       time.sleep(1)
       a += 1
    print("Tempo acabou. Passaram-se", a, "segundos.")

if Tipo_tempo == 2:
    minutos = int(input('quantos minutos?: '))
    b = 0
    while b < minutos:
        print(b)
        time.sleep(60)
        b += 1
    print("Tempo acabou. Passaram-se", b, "minutos.")

 