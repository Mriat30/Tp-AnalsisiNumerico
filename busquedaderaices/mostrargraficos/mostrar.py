import numpy as np
import matplotlib.pyplot as plt

def funciones(funcion):
    x = np.linspace(0, 3, 1000)

    y = funcion(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, label='f1(x)')
    ax.axhline(y=0, color='black', linestyle='--')
    ax.axvline(x=0, color='black', linestyle='--')

    ax.set_xlabel('x')
    ax.set_ylabel('f1(x)')
    ax.set_title('Gráfico de f1(x)')

    ax.legend(["f(x)"])
    plt.show()



def tablas(tablaDeResultados, ejeHorizontal, ejeVertical, titulo):

    resultados = np.array(tablaDeResultados) #Convierte la lista de tuplas tablaDeResultados(iteracion, valorBuscado)
    x = resultados[:, 0]
    y = resultados[:, 1]

    fig, ax = plt.subplots()

    ax.plot(x, y, label=str(ejeVertical))
    ax.axhline(y=0, color='black', linestyle='--')
    ax.axvline(x=0, color='black', linestyle='--')

    ax.set_xlabel(str(ejeHorizontal))
    ax.set_ylabel(str(ejeVertical))
    ax.set_title(str(titulo))

    ax.legend([str(ejeVertical)])
    plt.show()