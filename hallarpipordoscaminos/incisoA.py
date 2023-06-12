# Método de Newton-Raphson, defino f(x)=sen(x), tal que cuando busque la raíz llego a un valor aproximado a pi. sen(pi)=0
import math

def nr(p0):

  pi = math.pi
  n = 1

  while p0  != pi:
    pn = p0 - (math.sin(p0))/(math.cos(p0))
    n += 1
    p0 = pn

  return n,p0

def resolver():

  n,p0 = nr(3)
  print("pi vale:", p0)
  print("Se hicieron", n, "interaciones y se econtró en p", n)

