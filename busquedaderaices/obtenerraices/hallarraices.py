from busquedaderaices.obtenerraices import metodos
from scipy.optimize import brentq

SEMILLANR = 0.5
SEMIlLANRF3 = 1


def raizRealDeF(f, a, b):
    return brentq(f, a, b)

def hallarRaices(f, a, b, tolerancia):
    
    semilla = (a + b)/2
    tablaDeResultadosPorMetodo = []
    tablaDeResultadosPorMetodo.append(metodos.biseccion(f.funcion, a, b, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.puntoFijo(f.g, semilla, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.secante(f.funcion, a, b, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.newtonraphson(f.funcion, f.derivada, SEMIlLANRF3, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.nrmodificado(f.funcion, f.derivada, f.derivadaSegunda, SEMIlLANRF3, tolerancia))
    nombresDeLosMetodos = ("Biseccion", "Punto fijo", "Secante", "Newton-Raphson","N-R modificado" )
    tabla = list(zip(nombresDeLosMetodos, tablaDeResultadosPorMetodo))
    return tabla
