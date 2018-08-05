def sum_of_odd_squares(n):
    squares = [i*i for i in range(1, n+1)]
    odd_sum = 0;
    for j in squares:
        if j % 2 == 1:
            odd_sum += j
    return odd_sum
