def minmax(data):
    # takes a sequence of one or more numbers and returns the smallest and largest numbers
    # return a tuple with a length of two
    # do not use built-in min or max
    min_val = data[0]
    max_val = data[0]
    for i in range(len(data)):
        if min_val > data[i]:
            min_val = data[i]
        if max_val < data[i]:
            max_val = data[i]
    return min_val, max_val
