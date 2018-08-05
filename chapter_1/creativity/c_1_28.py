from math import pow

def norm(v, p = 2):
    sum_of_squares = sum([ v[i]**p for i in range(len(v)) ])
    if (p != 0):
        return pow(sum_of_squares, (1/p))
