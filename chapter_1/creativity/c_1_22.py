def dot_product(a, b):
    # takes two int arrays a and b of length n
    # returns the dot product of a & b
    if len(a) == len(b):
        return sum([a[i]*b[i] for i in range(len(a))])
