import time

try:
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
        secs = minutos * 60
        b = 0
        while b < secs:
            print(b)
            time.sleep(1)
            b += 1
        if minutos < 2:
            print("Tempo acabou. Passou-se ", minutos, "minuto.")
        else:
            print("Tempo acabou. Passaram-se ", minutos, "minutos.")
    else: 
        print("Opção invalida.")
except:
    print("Digito invalido.")
