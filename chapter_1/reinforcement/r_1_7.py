def sum_of_odd_squares(n):
    return sum([i*i for i in range(1, n+1) if (i*i) % 2 == 1])

