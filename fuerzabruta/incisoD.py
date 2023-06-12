import matplotlib.pyplot as plt
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

    bins = range(0, max(intentos_totales), 10)
    plt.hist(intentos_totales, bins=bins, edgecolor='black')
    plt.xlabel('Cantidad de intentos')
    plt.ylabel('Frecuencia')
    plt.show()

