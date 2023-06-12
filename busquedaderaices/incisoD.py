from mostrargraficos import mostrar
from funciones import f1
from funciones import f2
from funciones import f3
from obtenerraices import hallarraices
import math

def calcularConstantesAsintoticas(tablaDeRaices):
    constantesAsintoticas = [(tablaDeRaices[0][0], tablaDeRaices[0][1])]

    for i in range(1, len(tablaDeRaices) - 1):
        iterationActual = tablaDeRaices[i][0]  # Valor de la iteración n
        xActual = tablaDeRaices[i][1]  # Valor de la raíz en la iteración n
        xAnterior = tablaDeRaices[i - 1][1]  # Valor de la raíz en la iteración n-1
        xSiguiente = tablaDeRaices[i + 1][1]  # Valor de la raíz en la iteración n+1

        valorDeConstanteAsintotica = (xSiguiente - xActual) / (
                    xActual - xAnterior)  # Calcula la constante asintótica en la iteracion n
        constantesAsintoticas.append((iterationActual,
                                      valorDeConstanteAsintotica))  # Almacena el valor de la iteración junto con la constante asintótica

    return constantesAsintoticas


def calcularOrdenDeConvergencia(tablaDeRaices):
    ordenesDeConvergencia = [(tablaDeRaices[1][0], tablaDeRaices[1][1])]

    for i in range(2, len(tablaDeRaices) - 1):
        iteracionActual = tablaDeRaices[i][0]  # Valor de la iteración i
        xActual = tablaDeRaices[i][1]  # Valor de la raíz en la iteración i
        xAnterior = tablaDeRaices[i - 1][1]  # Valor de la raíz en la iteración i-1
        xAnteriorDelAnterior = tablaDeRaices[i - 2][1]  # Valor de la raíz en la iteración i-2
        xSiguiente = tablaDeRaices[i + 1][1]

        termino1 = (xSiguiente - xActual) / (xActual - xAnterior)
        termino2 = (xActual - xAnterior) / (xAnterior - xAnteriorDelAnterior)
        if(termino1 > 0) and (termino2 > 0):
            p = round(math.log(termino1, 10) / math.log(termino2, 10))
            ordenesDeConvergencia.append(
                (iteracionActual, p))  # Almacena el valor de la iteración junto con el orden de convergencia

    return ordenesDeConvergencia

def calcularLog10DeErrorLocal(tablaDeRaices):
    errorLocal = [(tablaDeRaices[0][0], tablaDeRaices[0][1])]

    for i in range(1,len(tablaDeRaices)):
        iteracionActual = tablaDeRaices[i][0]
        errorActual = abs(tablaDeRaices[i][1] - tablaDeRaices[i - 1][1])
        errorLocal.append((iteracionActual, math.log(errorActual, 10)))
    return errorLocal

def calcularLog10DeRaizCanidataMenosReal(tablaDeRaices, xReal):
    error = [(tablaDeRaices[0][0], tablaDeRaices[0][1])]

    for i in range(1,len(tablaDeRaices)):
        iteracionActual = tablaDeRaices[i][0]
        errorActual = abs(tablaDeRaices[i][1] - xReal)
        if errorActual > 0:
            error.append((iteracionActual, math.log(errorActual, 10)))
    return error

def graficarPorFuncion(tablaDeResultados ,funcion, xReal):

    for metodo in tablaDeResultados:
        mostrar.tablas(calcularOrdenDeConvergencia(metodo[1]), 'Iteraciones', 'Orden de convergencia P',metodo[0]+' de la funcion '+ funcion)
        mostrar.tablas(calcularConstantesAsintoticas(metodo[1]), 'Iteraciones', 'Constante asintotica λ',metodo[0]+' de la funcion '+ funcion)
        mostrar.tablas(calcularLog10DeErrorLocal(metodo[1]), 'Iteraciones', 'log10(/∆x/)', metodo[0]+' de la funcion '+ funcion)
        mostrar.tablas(calcularLog10DeRaizCanidataMenosReal(metodo[1], xReal), 'Iteraciones', 'log10(/xCandidata − xReal/)', metodo[0]+' de la funcion'+funcion)



def resolver():

    graficarPorFuncion(hallarraices.hallarRaices(f1, 0, 3, 1e-13), 'f1(x)', hallarraices.raizRealDeF(f1.funcion, 0, 3))
    graficarPorFuncion(hallarraices.hallarRaices(f2, 0, 3, 1e-13), 'f2(x)', hallarraices.raizRealDeF(f2.funcion, 0, 3))
    graficarPorFuncion(hallarraices.hallarRaices(f3, 0, 1.5, 1e-13), 'f3(x)', hallarraices.raizRealDeF(f3.funcion, 0, 1.5))


resolver()









