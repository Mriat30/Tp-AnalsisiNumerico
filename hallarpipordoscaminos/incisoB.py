
def leibniz_pi(n):
    s = 0
    for i in range(n):
        s += (-1)**i / (2*i+1)
    pi_approx = 4 * s
    return pi_approx


def resolver():
    # Definimos el número de términos de la serie
    n = 100000

    pi_approx = leibniz_pi(n)

    print("Valor aproximado de pi:", pi_approx)