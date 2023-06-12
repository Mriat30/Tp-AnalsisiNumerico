from funciones import f1
from funciones import f2
from funciones import f3
from obtenerraices import hallarraices


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

def mostrarTabla(f, tolerancia, tablaDeResultados):
    
    print("Funcion utilizada:", str(f.funcion), "Tolerancia utilizada: ", tolerancia)

    for metodo in tablaDeResultados:   #recorro cada metodo iterativo utilizado por la funcion determinada
        print("---------------------------------------------------------")
        print("Nombre del metodo: ", metodo[0])
        print("---------------------------------------------------------")
        print("| n |  Valor de la raiz                                  ")
        print("---------------------------------------------------------")
        resultados = metodo[1]
        if(len(resultados)) < 15:
            for resultado in resultados: #recorro cada iteracion del metodo determinado
                print("|", resultado[0] ,"|",resultado[1])
        
        else:
            for resultado in resultados[:5]:
                print("|", resultado[0], "|", resultado[1])

            for resultado in resultados[-5:]:
                print("|", resultado[0] ,"|",resultado[1])


def resolver():

    mostrarTabla(f1, TOLERANCIA_1, hallarraices.hallarRaices(f1, 0, 3, TOLERANCIA_1))
    print("\n\n")
    mostrarTabla(f1, TOLERANCIA_2, hallarraices.hallarRaices(f1, 0, 3, TOLERANCIA_2))
    print("\n\n\n")
    mostrarTabla(f2, TOLERANCIA_1, hallarraices.hallarRaices(f2, 0, 3, TOLERANCIA_1))
    print("\n\n")
    mostrarTabla(f2, TOLERANCIA_2, hallarraices.hallarRaices(f2, 0, 3, TOLERANCIA_2))
    print("\n\n\n")
    mostrarTabla(f3, TOLERANCIA_1, hallarraices.hallarRaices(f3, 0, 1.5, TOLERANCIA_1))
    print("\n\n")
    mostrarTabla(f3, TOLERANCIA_2, hallarraices.hallarRaices(f3, 0, 1.5, TOLERANCIA_2))

resolver()

