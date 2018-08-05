def arithmetic(a, b, c):
    # takes integers a, b, & c
    # determines if it can be used for a+b=c, a=b-c, OR a*b=c
    first = True if a+b == c else False
    second = True if a == b-c else False
    third = True if a*b == c else False
    return (first or second or third)
