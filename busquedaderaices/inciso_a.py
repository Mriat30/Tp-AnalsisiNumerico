import numpy as np
import matplotlib.pyplot as plt
from funciones import f1
from funciones import f2
from funciones import f3

#(a) Graficar las funciones en el intervalo de interes

def graficof1():
    
    x_values = np.linspace(0, 3, 1000)

    y_values = f1.funcion(x_values)


    fig, ax = plt.subplots()


    ax.plot(x_values, y_values, label='f1(x)')
    ax.axhline(y=0, color='black', linestyle='--')
    ax.axvline(x=0, color='black', linestyle='--')

    ax.set_xlabel('x')
    ax.set_ylabel('f1(x)')
    ax.set_title('Gráfico de f1(x)')



    ax.legend()
    plt.show()

def graficof2():

    x_values = np.linspace(0, 3, 1000)

    y_values = f2.funcion(x_values)

    fig, ax = plt.subplots()

    ax.plot(x_values, y_values, label='f2(x)')
    ax.axhline(y=0, color='black', linestyle='--')
    ax.axvline(x=0, color='black', linestyle='--')

    ax.set_xlabel('x')
    ax.set_ylabel('f2(x)')
    ax.set_title('Gráfico de f2(x)')

    ax.legend()
    plt.show()

def graficof3():

    e = np.e


    x_values = np.linspace(0, 3, 1000)

    y_values = f3(x_values)

    fig, ax = plt.subplots()

    ax.plot(x_values, y_values, label='f3(x)')
    ax.axhline(y=0, color='black', linestyle='--')
    ax.axvline(x=0, color='black', linestyle='--')

    ax.set_xlabel('x')
    ax.set_ylabel('f3(x)')
    ax.set_title('Gráfico de f3(x)')

    ax.legend()
    plt.show()


