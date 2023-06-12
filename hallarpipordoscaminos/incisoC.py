import numpy as np
from incisoB import leibniz_pi
import math

def nRaphson(iteraciones, p0):
  for i in range(iteraciones):
    p0 = p0 - (math.sin(p0))/(math.cos(p0))
  return p0

def resolver():
    iteraciones = [10, 100, 1000, 10000, 100000]

    for iteracion in iteraciones:
        print(f"Valor aproximado de pi con {iteracion}:", np.float32(leibniz_pi(iteracion)))

    print("\n\n\n")

    p0 = 3
    for iteracion in iteraciones:
        print(f"Valor aproximado de pi con {iteracion}:", np.float32(nRaphson(iteracion, p0)))
