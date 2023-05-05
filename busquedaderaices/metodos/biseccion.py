ITERACIONESMAXIMAS = 100

def biseccion(f, a, b, tolerancia):

    # Se inicializan los valores de los extremos del intervalo, la lista de aproximaciones y el número de iteraciones.
    a_n = a
    b_n = b
    i = 0
    raices = [(a_n + b_n) / 2]
    
    while i < ITERACIONESMAXIMAS:
        # Se calcula el punto medio del intervalo actual.
        p_n = (a_n + b_n) / 2
        
        # Se comprueba si se ha alcanzado la tolerancia deseada.
        if abs(b_n - a_n) < tolerancia:
            return raices, i
        
        # Se comprueba si se ha alcanzado el número máximo de iteraciones permitidas.
        if i == ITERACIONESMAXIMAS:
            raise Exception(f"No se pudo calcular la raíz en {ITERACIONESMAXIMAS} iteraciones.")
        
        # Se decide en qué mitad del intervalo se encuentra la raíz.
        if f(a_n) * f(p_n) < 0:
            b_n = p_n
        else:
            a_n = p_n
        
        # Se añade la nueva aproximación a la lista.
        raices.append((a_n + b_n) / 2)
        
        # Se incrementa el contador de iteraciones.
        i += 1
    
    # Se retorna la lista de aproximaciones y el número de iteraciones realizadas.
    return raices