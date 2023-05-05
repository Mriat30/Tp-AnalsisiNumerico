ITERACIONESMAXIMAS = 100

def newtonraphson(f, fDerivada, p0, tolerancia):
    listaDeRaices = []
    pAnterior = p0
    listaDeRaices.append(pAnterior)
    valorMinimo = 1e-20

    i = 1
    while ( i < ITERACIONESMAXIMAS):
        if abs(fDerivada(pAnterior)) < valorMinimo:
            print ("La derivada se anula en un punto candidato de la iteracion", i)

        pActual = pAnterior - f(pAnterior)/fDerivada(pAnterior)

        if abs(pActual- pAnterior) < tolerancia:
            return listaDeRaices
        
        listaDeRaices.append(pActual)
        i = i + 1
        pAnterior = pActual
    
    raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")