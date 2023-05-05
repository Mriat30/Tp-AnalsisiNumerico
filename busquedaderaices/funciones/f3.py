import math

def funcion(x):
    return (x - 0.9)*math.e**(-4*(x-0.9)**2)

def derivada(x):
    return ((-8*x + 7.2)*(x - 0.9) + 1)*math.e**(-4*(x-0.9)**2)

def derivadaSegunda(x):
    return 64*(-0.3915 + 2.055*x - 2.7*x**2 + x**3)*math.e**(-4*(x-0.9)**2)