import metodos

TOLERANCIA_1 = 1e-5
TOLERANCIA_2 = 1e-13
SEMILLANR = 0.5

def hallarRaices(f, a, b, tolerancia):
    
    semilla = (a + b)/2
    tablaDeResultadosPorMetodo = []
    tablaDeResultadosPorMetodo.append(metodos.biseccion(f.funcion, a, b, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.puntoFijo(f.g, semilla, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.secante(f.funcion, a, b, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.newtonraphson(f.funcion, f.fDerivada, SEMILLANR, tolerancia))
    tablaDeResultadosPorMetodo.append(metodos.nrmodificado(f.funcion, f.fDerivada, f.fDerivadaSegunda, SEMILLANR, tolerancia))
    nombresDeLosMetodos = ("Biseccion", "Punto fijo", "Secante", "Newton-Raphson","N-R modificado" )
    tabla = list(zip(nombresDeLosMetodos, tablaDeResultadosPorMetodo))
    return tabla