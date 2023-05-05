ITERACIONESMAXIMAS = 100

def secante(f, x0, x1, tolerancia):

    # Se inicializan los valores de la aproximación de la raíz, la lista de aproximaciones y el número de iteraciones.
    xn_1 = x0
    xn = x1
    i = 0
    aproximaciones = [xn_1, xn]
    
    while i < ITERACIONESMAXIMAS:
        # Se calcula el valor de la siguiente aproximación de la raíz.
        xn_1, xn = xn, xn - f(xn) * (xn - xn_1) / (f(xn) - f(xn_1))
        i += 1
        
        # Se añade la nueva aproximación a la lista.
        aproximaciones.append(xn)
        
        # Se comprueba el criterio de parada.
        if abs(xn - xn_1) < tolerancia:
            return aproximaciones
        
    # Si se alcanza el número máximo de iteraciones permitidas, se lanza una excepción.
    raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")