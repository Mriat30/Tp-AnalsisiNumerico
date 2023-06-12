import random

def resolver():
    intentos_totales = []
    for i in range(100000):
        clave = random.randint(100, 999)
        intentos = 0
        for j in range(100, 1000):
            intentos += 1
            if j == clave:
                break
        intentos_totales.append(intentos)
    print("Intentos promedio:", sum(intentos_totales) / len(intentos_totales))


