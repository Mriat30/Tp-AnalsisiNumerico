import random

def resolver():
    clave = random.randint(100, 999)
    intentos = 0
    for i in range(100, 1000):
        intentos += 1
        if i == clave:
            print("La clave es:", i)
            break
    print("Se necesitaron", intentos, "intentos.")