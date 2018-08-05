def sum_of_squares(n):
    # takes a positive integer n 
    # returns the sum of the squares of all positive integers smaller than n
    squares = [i*i for i in range(1, n+1)]
    return sum(squares)
