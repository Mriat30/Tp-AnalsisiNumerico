import math

def nRaphson(iteraciones, p0):
  for i in range(iteraciones):
    p0 = p0 - (math.sin(p0))/(math.cos(p0))
  return p0


def resolver():
  p0 = 3
  error = nRaphson(100000, p0) - nRaphson(99999, p0)
  print(error)



