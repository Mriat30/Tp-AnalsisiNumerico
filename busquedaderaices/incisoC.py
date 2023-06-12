from obtenerraices.hallarraices import raizRealDeF
from funciones import f1
from funciones import f2
from funciones import f3

def resolver():
    
    print("La raiz real de f1 es:" , raizRealDeF(f1.funcion, 0, 3))
    print("La raiz real de f1 es:" , raizRealDeF(f2.funcion, 0, 3))
    print("La raiz real de f1 es:" , raizRealDeF(f3.funcion, 0, 3))

resolver()