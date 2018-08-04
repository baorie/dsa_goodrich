def is_even(k):
    # Takes an integer value and returns True if k is even and False otherwise
    # Function cannot use multiplication, modulo, or division operators
    # Use a bitwise operator ( k & 1 ) will return 1 if odd 
    if int(k) & 1 : 
        print(str(k) + ' is odd')
        return False
    else:
        print(str(k) + ' is even')
        return True
