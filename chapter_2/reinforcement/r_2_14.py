class Vector:
    """ Represent a vector in a multidimensional space."""
    def __init__(self, d):
        """ Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """ Return the dimension of the vector."""
        return len(self._coords)
    
    def __getitem__(self, j):
        """ Return jth coordinate of vector."""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """ Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """ Return sum of two vectors. """
        if len(self) != len(other): #relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self)) #start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self, other):
        """ Return difference of two vectors. """
        if len(self) != len(other): #relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self)) #start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __neg__(self):
        """ Returns a new vector whose coordinates are all the negated values of current """
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = (-1) * self[j]
        return result

    def __mul__(self, other):
        """ Returns a new vector multiplied by specified scalar"""
        if not isinstance(other, (int, float)):
            raise TypeError('Scalar must be numeric')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other * self[j]
        return result
    
    def __rmul__(self, other):
        """ Returns a new vector multiplied by specified scalar but object on the right side. """
        if not isinstance(other, (int, float)):
            raise TypeError('Scalar must be numeric')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other * self[j]
        return result

    def __eq__(self, other):
        """ Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """ Return True if vector differs from other ."""
        return not self == other # rely on existing __eq__ definition

    def __str__(self):
        """ Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>' #adapt list rpresentation
    
    def dot_product(self, other):
        """ Return the dot product of two vectors. """
        if len(self) != len(other): #relies on __len__ method
            raise ValueErroR('dimensions must agree')
        return sum([ self[i]*other[i] for i in range(len(self))])
        
if __name__ == "__main__":
    vec1 = Vector(3)
    vec2 = Vector(3)
    for i in range(len(vec1)):
        vec1[i] = 1
        vec2[i] = 2
    print(vec1, vec2)
    print(vec1.dot_product(vec2))
