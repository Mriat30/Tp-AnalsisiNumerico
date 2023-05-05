import metodos
from funciones import f1
from funciones import f2
from funciones import f3

TOLERANCIA_1 = 1e-5
TOLERANCIA_2 = 1e-13
SEMILLANR = 0.5

#b) Halle para cada una de ellas la ra´ız en el intervalo indicado mediante los metodos vistos en
#clase:
#Bisecci´on
#Punto Fijo
#Secante
#Newton-Raphson
#Newton-Raphson modificado
#Use para todos los metodos como criterio de parada las siguientes diferencia entre dos iteraciones sucesivas:
#1 · 10−5
#1 · 10−13
#para Newton-Raphson use semilla x0 = 0.5.
#Mostrar en una tabla por cada m´etodo los resultados obtenidos (en caso que se obtengan
#muchas iteraciones se pueden mostrar las primeras 5 y las ´ultimas 5).

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

def mostrarTabla(f, tolerancia, tablaDeResultados):
    
    print("Funcion utilizada:", str(f.funcion), "Tolerancia utilizada: ", tolerancia)

    for metodo in tablaDeResultados:   #recorro cada metodo iterativo utilizado por la funcion determinada
        print("---------------------------------------------------------")
        print("Nombre del metodo: ", metodo[0])
        print("---------------------------------------------------------")
        print("| n |  Valor de la raiz                                  ")
        print("---------------------------------------------------------")
        resultados = metodo[1]
        i = 0
        if(len(resultados)) < 15:
            for iteracion in resultados: #recorro cada iteracion del metodo determinado
                print("|", i, "|", iteracion[i])
                i += 1        
        
        else:
            for i in range(0, 5):
                print("|", i, "|", iteracion[i])
                i += 1        
            for i in range(len(resultados) - 5, len(resultados)):
                print("|", i, "|", iteracion[i])
                i += 1  


def resolver():

    mostrarTabla(f1, TOLERANCIA_1, hallarRaices(f1, 0, 3, TOLERANCIA_1))
    mostrarTabla(f1, TOLERANCIA_2, hallarRaices(f1, 0, 3, TOLERANCIA_2))

    mostrarTabla(f2, TOLERANCIA_1, hallarRaices(f2, 0, 3, TOLERANCIA_1))
    mostrarTabla(f2, TOLERANCIA_2, hallarRaices(f2, 0, 3, TOLERANCIA_2))

    mostrarTabla(f3, TOLERANCIA_1, hallarRaices(f3, 0, 3, TOLERANCIA_1))
    mostrarTabla(f3, TOLERANCIA_2, hallarRaices(f3, 0, 3, TOLERANCIA_2))


