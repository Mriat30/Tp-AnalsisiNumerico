from busquedaderaices.obtenerraices import metodos
import scipy.optimize as sc

TOLERANCIA_1 = 1e-5
TOLERANCIA_2 = 1e-13
SEMILLANR = 0.5

def raizRealDeF(f):
    raiz = sc.root(f.funcion, 0)
    return raiz

def hallarRaices(f, a, b, tolerancia):
    
    semilla = (a + b)/2
    tablaDeResultadosPorMetodo = []
    tablaDeResultadosPorMetodo.append(metodos.biseccion(f.funcion, a, b, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.puntoFijo(f.g, semilla, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.secante(f.funcion, a, b, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.newtonraphson(f.funcion, f.derivada, SEMILLANR, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.nrmodificado(f.funcion, f.derivada, f.derivadaSegunda, SEMILLANR, tolerancia))
    nombresDeLosMetodos = ("Biseccion", "Punto fijo", "Secante", "Newton-Raphson","N-R modificado" )
    tabla = list(zip(nombresDeLosMetodos, tablaDeResultadosPorMetodo))
    return tabla