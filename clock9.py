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

def valor_convertido(tipo, valor):
    if tipo == 1:
        return valor
    elif tipo == 2: #se é minuto
        return valor * 60

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

def countdown(a):
    while a > 0:
        print(a)
        time.sleep(1)
        a -= 1

def mensagem_final(tipo, valor, valororiginal):
    if tipo == 1:
        plural = "passou" if valor == 1 else "passaram-se"
        unidade = "segundo" if valor == 1 else "segundos"
        print(f"Tempo acabou, {plural} {valor} {unidade}.")
        quit()

    elif tipo == 2:
        plural = "passou" if valororiginal == 1 else "passaram-se"
        unidade = "minuto" if valororiginal == 1 else "minutos"
        print(f"Tempo acabou, {plural} {valororiginal} {unidade}.")
        quit()


def passar_tempo(a, b, c): ## a = tipo de tempo, b = quantidade de tempo
    countdown(b)
    mensagem_final(a, b, c)


tipo = minuto_ou_hora()
tmp = tempo(tipo)
valorconvertido = valor_convertido(tipo, tmp)
passar_tempo(tipo, valorconvertido, tmp)
