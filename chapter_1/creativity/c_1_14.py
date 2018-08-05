def odd_product(data):
    # takes a sequence of integers
    # determines if theres a distinct pair of numbers whose product is odd
    distinct = set(data)
    for i in distinct:
        for j in distinct:
            if i != j and (i*j) % 2 == 1:
                return i, j

