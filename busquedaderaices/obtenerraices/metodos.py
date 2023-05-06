ITERACIONESMAXIMAS = 100

def biseccion(f, a, b, tolerancia):
    # Se inicializan los valores de los extremos del intervalo, la lista de aproximaciones y el número de iteraciones.
    a_n = a
    b_n = b
    i = 0
    raices = [(i, (a_n + b_n) / 2)]

    while i < ITERACIONESMAXIMAS:
        # Se calcula el punto medio del intervalo actual.
        p_n = (a_n + b_n) / 2

        # Se comprueba si se ha alcanzado la tolerancia deseada.
        if abs(b_n - a_n) < tolerancia:
            return raices

        # Se comprueba si se ha alcanzado el número máximo de iteraciones permitidas.
        if i == ITERACIONESMAXIMAS:
            raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")

        # Se decide en qué mitad del intervalo se encuentra la raíz.
        if f(a_n) * f(p_n) < 0:
            b_n = p_n
        else:
            a_n = p_n

        # Se incrementa el contador de iteraciones.
        i += 1

        # Se añade la nueva aproximación a la lista.
        raices.append((i, (a_n + b_n) / 2))

    # Se retorna la lista de aproximaciones y el número de iteraciones realizadas.
    return raices



def newtonraphson(f, derivada, p0, tolerancia):

    pAnterior = p0
    i = 0
    listaDeRaices = [(i, pAnterior)]
    valorMinimo = 1e-20

    while ( i < ITERACIONESMAXIMAS):

        if abs(derivada(pAnterior)) < valorMinimo:
            print ("La derivada se anula en un punto candidato de la iteracion", i)

        pActual = pAnterior - f(pAnterior)/derivada(pAnterior)

        if abs(pActual - pAnterior) < tolerancia:
            return listaDeRaices

        i += 1
        listaDeRaices.append((i, pActual))
        pAnterior = pActual

    raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")

def nrmodificado(f, derivada, derivadaSegunda, p0, tolerancia):

    i = 0
    pAnterior = p0
    listaDeRaices = [(i, pAnterior)]
  

    while ( i < ITERACIONESMAXIMAS):
        numerador = f(pAnterior)*derivada(pAnterior)
        denominador = derivada(pAnterior)**2 - f(pAnterior)*derivadaSegunda(pAnterior)
        pActual = pAnterior - numerador/denominador

        if abs(pActual- pAnterior) < tolerancia:
            return listaDeRaices

        i += 1
        listaDeRaices.append((i, pActual))
        pAnterior = pActual
    
    raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")


def puntoFijo(g, po, tolerancia):

    i = 0
    pActual = po
    raices = [(i,pActual)]

    while i < ITERACIONESMAXIMAS:
        pAnterior = pActual
        pActual = g(pActual)

        if abs(pActual - pAnterior) < tolerancia:
            return raices

        raices.append((i,pActual))
        i += 1

    raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")


def secante(f, x0, x1, tolerancia):
    # Se inicializan los valores de la aproximación de la raíz, la lista de aproximaciones y el número de iteraciones.
    xn_1 = x0
    xn = x1
    i = 0
    raices = [(i, [xn_1, xn])]

    while i < ITERACIONESMAXIMAS:
        # Se calcula el valor de la siguiente aproximación de la raíz.
        xn_1, xn = xn, xn - f(xn) * (xn - xn_1) / (f(xn) - f(xn_1))

        # Se comprueba el criterio de parada.
        if abs(xn - xn_1) < tolerancia:
            return raices

        i += 1
        raices.append((i, xn))

    # Si se alcanza el número máximo de iteraciones permitidas, se lanza una excepción.
    raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")
