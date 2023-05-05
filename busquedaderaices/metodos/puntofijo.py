ITERACIONESMAXIMAS = 100

def puntofijo(g, po, tolerancia):
    
    pAnterior = po
    raices = [pAnterior]
    i = 0

    while i < ITERACIONESMAXIMAS:
        pActual = g(pAnterior)

        if abs(pActual - pAnterior) < tolerancia:
            return raices

        raices.append(pActual)
        i += 1
        pAnterior = pAnterior

    
    raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")