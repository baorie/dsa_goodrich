# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import collections

class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val

  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result
  
  def __mul__(self, other):
    """ Use runtime type checking to support both syntaxes u*v and u*k where u and v designate vector instances and k represents a number """
    if isinstance(other, Vector) and len(self) == len(other):
      # returns dot product
      return sum([ self[i]*other[i] for i in range(len(self)) ])
    if isinstance(other, (int, float)):
      result = Vector(len(self))
      for j in range(len(self)):
        result[j] = self[j] * other
      return result



  def __eq__(self, other):
    """Return True if vector has same coordinates as other."""
    return self._coords == other._coords

  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other             # rely on existing __eq__ definition

  def __str__(self):
    """Produce string representation of vector."""
    return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

  def __neg__(self):
    """Return copy of vector with all coordinates negated."""
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = -self[j]
    return result

  def __lt__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords < other._coords

  def __le__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords <= other._coords

if __name__ == '__main__':
  # the following demonstrates usage of a few methods
  v1 = Vector(3)
  v2 = Vector(3)
  for i in range(len(v1)):
    v1[i] = 1
    v2[i] = 1
  print("Multiply v1 by a number")
  res1 = v1*3
  print(res1)
  print("multiply v1 by v2 and get a dot product")
  dot = v1*v2
  print(dot)
