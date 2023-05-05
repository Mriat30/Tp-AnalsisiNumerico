ITERACIONESMAXIMAS = 100

def nrmodificado(f, fDerivada, fDerivadaSegunda, p0, tolerancia):
    listaDeRaices = []
    pAnterior = p0
    listaDeRaices.append(pAnterior)
  
    i = 1
    while ( i < ITERACIONESMAXIMAS):
        numerador = f(pAnterior)*fDerivada(pAnterior)
        denominador = fDerivada(pAnterior)**2 - f(pAnterior)*fDerivadaSegunda(pAnterior)
        pActual = pAnterior - numerador/denominador
        listaDeRaices.append(pActual)

        if abs(pActual- pAnterior) < tolerancia:
            return listaDeRaices
        i = i + 1
        pAnterior = pActual
    
    raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")